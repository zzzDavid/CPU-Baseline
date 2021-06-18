import torch.nn as nn
import torch
from time import perf_counter
from torchsummary import summary
import multiprocessing

class MobileNetV1(nn.Module):
    def __init__(self, ch_in, n_classes):
        super(MobileNetV1, self).__init__()

        def conv_bn(inp, oup, stride):
            return nn.Sequential(
                nn.Conv2d(inp, oup, 3, stride, 1, bias=False),
                nn.BatchNorm2d(oup),
                nn.ReLU(inplace=True)
                )

        def conv_dw(inp, oup, stride):
            return nn.Sequential(
                # dw
                nn.Conv2d(inp, inp, 3, stride, 1, groups=inp, bias=False),
                nn.BatchNorm2d(inp),
                nn.ReLU(inplace=True),

                # pw
                nn.Conv2d(inp, oup, 1, 1, 0, bias=False),
                nn.BatchNorm2d(oup),
                nn.ReLU(inplace=True),
                )

        self.model = nn.Sequential(
            conv_bn(ch_in, 32, 2),
            conv_dw(32, 64, 1),
            conv_dw(64, 128, 2),
            conv_dw(128, 128, 1),
            conv_dw(128, 256, 2),
            conv_dw(256, 256, 1),
            conv_dw(256, 512, 2),
            conv_dw(512, 512, 1),
            conv_dw(512, 512, 1),
            conv_dw(512, 512, 1),
            conv_dw(512, 512, 1),
            conv_dw(512, 512, 1),
            conv_dw(512, 1024, 2),
            conv_dw(1024, 1024, 1),
            nn.AdaptiveAvgPool2d(1)
        )
        self.fc = nn.Linear(1024, n_classes)

    def forward(self, x):
        x = self.model(x)
        x = x.view(-1, 1024)
        x = self.fc(x)
        return x

def test_latency(input_size=(1, 3, 224, 224), avg_run=100):
    torch.set_num_threads(1);
    model = MobileNetV1(ch_in=3, n_classes=1000).cpu()
    x = torch.randn(input_size, device="cpu")
    start = perf_counter()
    for _ in range(avg_run):
        model(x)
    end = perf_counter()
    ms = (end-start) * 1e3
    ms /= avg_run
    print(f"MobileNetV1 on CPU, threads = {torch.get_num_threads()}, number of CPU: {multiprocessing.cpu_count()}, latency = {ms} ms, averaged over {avg_run} runs.")    

if __name__=='__main__':
    # model check
#    model = MobileNetV1(ch_in=3, n_classes=1000)
    #summary(model, input_size=(3, 224, 224), device='cpu')
    test_latency()