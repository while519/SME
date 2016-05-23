#! /usr/bin/python
import sys
sys.path.append('/volatile/yuwu/git-repo/SME')
from FB15k_exp import *


launch(op='SME_bil', simfn='Dot', ndim=50, nhid=50, marge=1., lremb=0.01,
    lrparam=1., nbatches=100, totepochs=1000, test_all=10, neval=1000,
    savepath='FB15k_SME_bil', datapath='../data/')
