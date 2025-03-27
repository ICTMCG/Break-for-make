# B4M: Breaking Low-Rank Adapter for Making Content-Style Customization [ACM TOG 2025]

> **B4M: Breaking Low-Rank Adapter for Making Content-Style Customization**<br>
> Yu Xu<sup>1,2</sup>, Fan Tang<sup>1</sup>, Juan Cao<sup>1</sup>, Yuxin Zhang<sup>3</sup>, Oliver Deussen<sup>4</sup>, Weiming Dong<sup>3</sup>, Jintao Li<sup>1</sup>, Tong-Yee Lee<sup>5</sup> <br>
> <sup>1</sup>Institute of Computing Technology, Chinese Academy of Sciences, <sup>2</sup>University of Chinese Academy of Sciences, <sup>3</sup> Institute of Automation, Chinese Academy of Sciences, <sup>4</sup>University of Konstanz, <sup>5</sup>National Cheng Kung University


![](assets/teaser.png)

<a href='https://arxiv.org/abs/2403.19456'><img src='https://img.shields.io/badge/ArXiv-2403.19456-red'></a> 


>**Abstract**: <br>
>Personalized generation paradigms empower designers to customize visual intellectual properties with the help of textual descriptions by adapting pre-trained text-to-image models on a few images. Recent studies focus on simultaneously customizing content and detailed visual style in images but often struggle with entangling the two. In this study, we reconsider the customization of content and style concepts from the perspective of parameter space construction. Unlike existing methods that utilize a shared parameter space for content and style learning, we propose a novel framework that separates the parameter space to facilitate individual learning of content and style by introducing "partly learnable projection" (PLP) matrices to separate the original adapters into divided sub-parameter spaces. A "break-for-make" customization learning pipeline based on PLP is proposed: we first "break" the original adapters into "up projection" and "down projection" for content and style concept under orthogonal prior and then "make" the entity parameter space by reconstructing the content and style PLPs matrices by using Riemannian precondition to adaptively balance content and style learning. Experiments on various styles, including textures, materials, and artistic style, show that our method outperforms state-of-the-art single/multiple concept learning pipelines regarding content-style-prompt alignment.


## More of our results
![](assets/more_results.png)

## Citation
If you make use of our work, please cite our paper:

```
@article{xu2024break,
  title={Break-for-make: Modular low-rank adaptations for composable content-style customization},
  author={Xu, Yu and Tang, Fan and Cao, Juan and Zhang, Yuxin and Deussen, Oliver and Dong, Weiming and Li, Jintao and Lee, Tong-Yee},
  journal={arXiv preprint arXiv:2403.19456},
  year={2024}
}
```
