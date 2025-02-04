class Config(object):
    env = 'default'
    backbone = 'resnet18'
    classify = 'softmax'
    num_classes = 13938
    metric = 'arc_margin'
    easy_margin = False
    #use_se = False
    use_se = True
    loss = 'focal_loss'

    #display = False
    display = True
    finetune = False

    #train_root = '/data/Datasets/webface/CASIA-maxpy-clean-crop-144/'
    #train_list = '/data/Datasets/webface/train_data_13938.txt'
    train_root = 'data/Datasets/webface/CASIA-WebFace'
    train_list = 'data/Datasets/webface/cleaned list.txt'
    #val_list = '/data/Datasets/webface/val_data_13938.txt'

    test_root = '/data1/Datasets/anti-spoofing/test/data_align_256'
    test_list = 'test.txt'

    lfw_root = 'data/Datasets/lfw-align-128'
    lfw_test_list = 'lfw_test_pair.txt'

    checkpoints_path = 'checkpoints'
    load_model_path = 'models/resnet18.pth'
    test_model_path = 'checkpoints/resnet18_110.pth'
    save_interval = 2

    train_batch_size = 16  # batch size
    test_batch_size = 60

    input_shape = (1, 128, 128)

    optimizer = 'sgd'

    use_gpu = True  # use GPU or not
    #gpu_id = '0, 1'
    gpu_id = '0'
    #num_workers = 4  # how many workers for loading data
    num_workers = 0  # how many workers for loading data
    print_freq = 100  # print info every N batch

    debug_file = '/tmp/debug'  # if os.path.exists(debug_file): enter ipdb
    result_file = 'result.csv'

    max_epoch = 50
    lr = 1e-1  # initial learning rate
    lr_step = 10
    lr_decay = 0.95  # when val_loss increase, lr = lr*lr_decay
    weight_decay = 5e-4
