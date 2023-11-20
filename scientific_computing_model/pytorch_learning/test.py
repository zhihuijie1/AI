import torch

if __name__ == '__main__':
    #test CUDA
    # print("support cuda ? ", torch.cuda.is_available())
    x = torch.tensor([10.0])
    #x = x.cuda()
    print(x)

    y = torch.randn(2,3)
    #y = y.cuda()
    print(y)

    z = x + y
    print(z)

    #test CUDNN
    from torch.backends import cudnn
    print("support cudnn ",cudnn.is_acceptable(x))

