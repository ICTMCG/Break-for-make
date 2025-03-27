
# B4M: Breaking Low-Rank Adapter for Making Content-Style Customization

![](assets/teaser.png)

<a href='https://arxiv.org/abs/2403.19456'><img src='https://img.shields.io/badge/ArXiv-2403.19456-red'></a> 


## Abstract
Personalized generation paradigms empower designers to customize visual intellectual properties with the help of textual descriptions by adapting pre-trained text-to-image models on a few images. Recent studies focus on simultaneously customizing content and detailed visual style in images but often struggle with entangling the two. In this study, we reconsider the customization of content and style concepts from the perspective of parameter space construction. Unlike existing methods that utilize a shared parameter space for content and style learning, we propose a novel framework that separates the parameter space to facilitate individual learning of content and style by introducing "partly learnable projection" (PLP) matrices to separate the original adapters into divided sub-parameter spaces. A "break-for-make" customization learning pipeline based on PLP is proposed: we first "break" the original adapters into "up projection" and "down projection" for content and style concept under orthogonal prior and then "make" the entity parameter space by reconstructing the content and style PLPs matrices by using Riemannian precondition to adaptively balance content and style learning. Experiments on various styles, including textures, materials, and artistic style, show that our method outperforms state-of-the-art single/multiple concept learning pipelines regarding content-style-prompt alignment.

## Pipeline
![](assets/pipeline.png)

## Comparison with baselines
![](assets/main_compare_1.png)
![](assets/main_compare_2.png)

## More of our results
![](assets/more_results.png)
