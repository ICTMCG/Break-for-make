from torch.optim.optimizer import Optimizer, required
import torch
import copy

class AdamWr(Optimizer):
    def __init__(self, params, lr=required, weight_decay=0, eps=1e-8, betas=(0.9, 0.999)):
        defaults = dict(lr=lr, weight_decay=weight_decay)
        super(AdamWr, self).__init__(params, defaults)
        num_params = sum([len(i['params']) for i in params])
        self.m = [0]*num_params
        self.v = [0]*num_params
        self.beta1 = betas[0]
        self.beta2 = betas[1]
        self.lr = lr
        self.t = 1
        self.eps = eps
    def __setstate__(self, state):
        super(AdamWr, self).__setstate__(state)

    def step(self, closure=None):
        """ Performs a single optimization step.
        Arguments:
            closure (callable, optional): A closure that reevaluates the model
                and returns the loss.
        """
        loss = None
        if closure is not None:
            loss = closure()

        idx = 0
        for group in self.param_groups:
            weight_decay = group['weight_decay']
            p0 = group['params'][0].data
            p1 = group['params'][1].data
            d_p0 = group['params'][0].grad.data
            d_p1 = group['params'][1].grad.data
            if torch.linalg.norm(p0.mm(p0.T))>1e-6:
                c1 = torch.inverse(p0.mm(p0.T)+group['reg']*torch.eye(p0.shape[0]).to(p0.device))
            else:
                c1 = torch.eye((p0.mm(p0.T)).shape[0]).to(p0.device)
            d_p1_scaled = d_p1.mm(c1)
            if torch.linalg.norm(p1.T.mm(p1))>1e-6:
                c0 = torch.inverse(p1.T.mm(p1)+group['reg']*torch.eye(p1.shape[1]).to(p1.device))
            else:
                c0 = torch.eye((p1.T.mm(p1)).shape[0]).to(p1.device)
            d_p0_scaled = (d_p0.T.mm(c0)).T
            self.m[idx] = self.beta1*self.m[idx] + (1-self.beta1)*d_p0_scaled
            self.v[idx] = self.beta2*self.v[idx] + (1-self.beta2)*d_p0_scaled**2
            m_hat = self.m[idx]/(1-self.beta1**self.t)
            v_hat = self.v[idx]/(1-self.beta2**self.t)
            p0.add_(m_hat/(torch.sqrt(v_hat)+self.eps), alpha=-group['lr'])
            idx += 1

            self.m[idx] = self.beta1*self.m[idx] + (1-self.beta1)*d_p1_scaled
            self.v[idx] = self.beta2*self.v[idx] + (1-self.beta2)*d_p1_scaled**2
            m_hat = self.m[idx]/(1-self.beta1**self.t)
            v_hat = self.v[idx]/(1-self.beta2**self.t)
            p1.add_(m_hat/(torch.sqrt(v_hat)+self.eps), alpha=-group['lr'])
            idx += 1
            if weight_decay != 0:
                p0.add_(-group['lr']*weight_decay, p0)
                p1.add_(-group['lr']*weight_decay, p1)
        self.t += 1

        return loss


class SGDr(Optimizer):
    def __init__(self, params, lr=required, weight_decay=0):
        defaults = dict(lr=lr, weight_decay=weight_decay)
        super(SGDr, self).__init__(params, defaults)
        num_params = sum([len(i['params']) for i in params])
        self.lr = lr

    def __setstate__(self, state):
        super(SGDr, self).__setstate__(state)
    
    def step(self, closure=None):
        """ Performs a single optimization step.
        Arguments:
            closure (callable, optional): A closure that reevaluates the model
                and returns the loss.
        """
        loss = None
        if closure is not None:
            loss = closure()

        idx = 0
        for group in self.param_groups:
            weight_decay = group['weight_decay']
            p0 = group['params'][0].data
            p1 = group['params'][1].data
            d_p0 = group['params'][0].grad.data
            d_p1 = group['params'][1].grad.data
            if weight_decay != 0:
                p0.add_(-group['lr']*weight_decay, p0)
                p1.add_(-group['lr']*weight_decay, p1)
            if torch.linalg.norm(p0.mm(p0.T))>1e-6:
                c1 = torch.inverse(p0.mm(p0.T)+group['reg']*torch.eye(p0.shape[0]).to(p0.device))
            else:
                c1 = torch.eye((p0.mm(p0.T)).shape[0]).to(p0.device)
            d_p1_scaled = d_p1.mm(c1)
            if torch.linalg.norm(p1.T.mm(p1))>1e-6:
                c0 = torch.inverse(p1.T.mm(p1)+group['reg']*torch.eye(p1.shape[1]).to(p1.device))
            else:
                c0 = torch.eye((p1.T.mm(p1)).shape[0]).to(p1.device)
            d_p0_scaled = (d_p0.T.mm(c0)).T
            p0.add_(d_p0_scaled, alpha=-group['lr'])
            p1.add_(d_p1_scaled, alpha=-group['lr'])

        return loss
            