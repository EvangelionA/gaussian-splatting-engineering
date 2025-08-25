<h1 align="center">gaussian-splatting-engineering</h1>
<p align="center">
  <img src="https://img.shields.io/github/languages/code-size/nanchengcyu/TechMindWave-backend" alt="code size"/>
  <img src="https://img.shields.io/badge/Spring%20Boot-2.5.4-brightgreen" alt="Spring Boot"/>
  <img src="https://img.shields.io/github/languages/count/nanchengcyu/TechMindWave-backend" alt="languages"/>
  <img src="https://img.shields.io/badge/Java-8-blue" alt="Java"/>
  <img src="https://img.shields.io/github/last-commit/nanchengcyu/TechMindWave-backend" alt="last commit"/><br>
  <img src="https://img.shields.io/badge/Author-nanchengyu-orange" alt="Author" />
  <a href="docs/README_ZH.md"><img src="https://img.shields.io/badge/Doc-中文版-white.svg" alt="ZH doc"/></a>
</p>
<hr>

# Introduction
  This repository aims to bridge the gap between academic research and industrial deployment of 3D Gaussian Splatting (3DGS) technology. While most existing papers focus on theoretical innovations, this project emphasizes:
1. **Engineering-oriented implementation**
   
2. **Steady performance optimization**
   
3. **Systematic documentation of practical workflows**

## TODO_LIST
- improvement
  - [ ] [ABS-GS](https://github.com/TY424/AbsGS)
  - [ ] [RAIN-GS](https://github.com/whuhxb/RAIN-GS)
- format support
  - [ ] [USDZ format](https://github.com/nv-tlabs/3dgrut) / [Omniverse](https://docs.nvidia.com/omniverse/index.html#get-started)
  - [ ] [SPZ format](https://github.com/nv-tlabs/3dgrut)
- doc support
  - [ ] pipeline Instructions (WIP)
  - [ ] [colmap](https://github.com/TY424/AbsGS)
    - [ ] [USER GUID]
  - [ ] [RealityCapture](https://github.com/TY424/AbsGS)
  - [ ] [KIRI](https://github.com/TY424/AbsGS)
  - [ ] 
  - [x] Play [Minecraft](https://www.minecraft.net)
  - [x] Play [Factorio](https://www.factorio.com) (WIP, but [PoC and demo available](https://github.com/moeru-ai/airi-factorio))
  - [x] Chat in [Telegram](https://telegram.org)
  - [x] Chat in [Discord](https://discord.com)
  - [ ] Memory
    - [x] Pure in-browser database support (DuckDB WASM | `pglite`)
    - [ ] Memory Alaya (WIP)
  - [ ] Pure in-browser local (WebGPU) inference


# Improvement Item Description
## Improverment
 paper | Introduction | 
 ---- | ---- 
 [ABS-GS](https://github.com/TY424/AbsGS) | Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification. 
 [RAIN-GS](https://github.com/TY424/AbsGS) | Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification.  


 
 
### [ABS-GS](https://github.com/TY424/AbsGS)
<details>
<summary><span style="font-weight: bold;">Abstract</span></summary>
Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification.
</details>

### [RAIN-GS](https://github.com/whuhxb/RAIN-GS)
<details>
<summary><span style="font-weight: bold;">Abstract</span></summary>
Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification.
</details>

## Format Support
 format | Introduction | 
 ---- | ---- 
 [USDZ](https://github.com/nv-tlabs/3dgrut) | Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification. 
 [SPZ](https://github.com/TY424/AbsGS) | Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification.  

### [USDZ](https://github.com/nv-tlabs/3dgrut)
<details>
<summary><span style="font-weight: bold;">Abstract</span></summary>
Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification.
</details>


### [SPZ]()
<details>
<summary><span style="font-weight: bold;">Abstract</span></summary>
Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification.
</details>


# Gaussian-Splatting PIPELINE
## Stage_1 : Accurate Camera Pose [*Crucial*]
bad pose bad result

不论是3DGS项目还是传统的空三项目、SFM、MVS等，前期的工作都是获取到足够准确的相机位姿，这一步至关重要，这一步的误差会直接影响到后续的重建结果。

传统主流的相机位姿获取方法有：

开源项目：

开源项目 | 商业免费 | 商业付费 | 移动端
 ---- | ---- | ---- | ----
 [COLMAP](https://github.com/colmap/colmap) (recommended) | [postshot](https://www.jawset.com/)(recommended)[User Guide](https://www.jawset.com/docs/d/Postshot+User+Guide)| [ContextCapture](https://www.contextcapture.com) | [KIRI](https://www.kiri.com)(recommended) 
 [openMVG](https://github.com/openMVG/openMVG) | [Reality Capture](https://www.realitycapture.com) | [大疆智图](https://www.dji.com/cn/products/enterprise/3d-surveying)|[Polyscam](https://www.polyscanner.com)
 [OpenSfM](https://github.com/mapillary/OpenSfM) |  | |[matterport](https://www.matterport.com)
 [MVS](https://github.com/colmap/colmap) |  | |


前馈网络框架：
1. [VGGT](https://github.com/autonomousvision/vggt)
2. [DUST3R](https://github.com/autonomousvision/duster)
3. [MAST3R](https://github.com/autonomousvision/master)
4. [FAST3R](https://github.com/autonomousvision/FASTER)
  


### [openMVG](https://github.com/openMVG/openMVG)
<details>
<summary><span style="font-weight: bold;">Abstract</span></summary>
Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification.
</details>

### [COLMAP](https://github.com/colmap/colmap)
<details>
<summary><span style="font-weight: bold;">Abstract</span></summary>


### Image Pose
### [openMVG](https://github.com/openMVG/openMVG)
<details>
<summary><span style="font-weight: bold;">Abstract</span></summary>
Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification.
</details>

### [COLMAP](https://github.com/colmap/colmap)
<details>
<summary><span style="font-weight: bold;">Abstract</span></summary>
We have limited resources for maintaining and updating the code. However, we have added a few new features since the original release that are inspired by some of the excellent work many other researchers have been doing on 3DGS. We will be adding other features within the ability of our resources.
</details>

## Stage_2 : Gaussian Splatting Training

**Update of October 2024**: We integrated [training speed acceleration](#training-speed-acceleration) and made it compatible with [depth regularization](#depth-regularization), [anti-aliasing](#anti-aliasing) and [exposure compensation](#exposure-compensation). We have enhanced the SIBR real time viewer by correcting bugs and adding features in the [Top View](#sibr-top-view) that allows visualization of input and user cameras.

## Stage_3 : Gaussian Splatting Application
### [SIBR](https://github.com/graphdeco-inria/sibr)
<details>
<summary><span style="font-weight: bold;">Abstract</span></summary>
</details>



## FAQ
- *Where do I get data sets, e.g., those referenced in ```full_eval.py```?* The MipNeRF360 data set is provided by the authors of the original paper on the project site. Note that two of the data sets cannot be openly shared and require you to consult the authors directly. For Tanks&Temples and Deep Blending, please use the download links provided at the top of the page. Alternatively, you may access the cloned data (status: August 2023!) from [HuggingFace](https://huggingface.co/camenduru/gaussian-splatting)


- *How can I use this for a much larger dataset, like a city district?* The current method was not designed for these, but given enough memory, it should work out. However, the approach can struggle in multi-scale detail scenes (extreme close-ups, mixed with far-away shots). This is usually the case in, e.g., driving data sets (cars close up, buildings far away). For such scenes, you can lower the ```--position_lr_init```, ```--position_lr_final``` and ```--scaling_lr``` (x0.3, x0.1, ...). The more extensive the scene, the lower these values should be. Below, we use default learning rates (left) and ```--position_lr_init 0.000016 --scaling_lr 0.001"``` (right).

| ![Default learning rate result](assets/worse.png "title-1") <!-- --> | <!-- --> ![Reduced learning rate result](assets/better.png "title-2") |
| --- | --- |

- *I'm on Windows and I can't manage to build the submodules, what do I do?* Consider following the steps in the excellent video tutorial [here](https://www.youtube.com/watch?v=UXtuigy_wYc), hopefully they should help. The order in which the steps are done is important! Alternatively, consider using the linked Colab template.

- *It still doesn't work. It says something about ```cl.exe```. What do I do?* User Henry Pearce found a workaround. You can you try adding the visual studio path to your environment variables (your version number might differ);
```C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64```
Then make sure you start a new conda prompt and cd to your repo location and try this;
```
conda activate gaussian_splatting
cd <dir_to_repo>/gaussian-splatting
pip install submodules\diff-gaussian-rasterization
pip install submodules\simple-knn
```

- *I'm on macOS/Puppy Linux/Greenhat and I can't manage to build, what do I do?* Sorry, we can't provide support for platforms outside of the ones we list in this README. Consider using the linked Colab template.

- *I don't have 24 GB of VRAM for training, what do I do?* The VRAM consumption is determined by the number of points that are being optimized, which increases over time. If you only want to train to 7k iterations, you will need significantly less. To do the full training routine and avoid running out of memory, you can increase the ```--densify_grad_threshold```, ```--densification_interval``` or reduce the value of ```--densify_until_iter```. Note however that this will affect the quality of the result. Also try setting ```--test_iterations``` to ```-1``` to avoid memory spikes during testing. If ```--densify_grad_threshold``` is very high, no densification should occur and training should complete if the scene itself loads successfully.

- *24 GB of VRAM for reference quality training is still a lot! Can't we do it with less?* Yes, most likely. By our calculations it should be possible with **way** less memory (~8GB). If we can find the time we will try to achieve this. If some PyTorch veteran out there wants to tackle this, we look forward to your pull request!


- *How can I use the differentiable Gaussian rasterizer for my own project?* Easy, it is included in this repo as a submodule ```diff-gaussian-rasterization```. Feel free to check out and install the package. It's not really documented, but using it from the Python side is very straightforward (cf. ```gaussian_renderer/__init__.py```).

- *Wait, but ```<insert feature>``` isn't optimized and could be much better?* There are several parts we didn't even have time to think about improving (yet). The performance you get with this prototype is probably a rather slow baseline for what is physically possible.

- *Something is broken, how did this happen?* We tried hard to provide a solid and comprehensible basis to make use of the paper's method. We have refactored the code quite a bit, but we have limited capacity to test all possible usage scenarios. Thus, if part of the website, the code or the performance is lacking, please create an issue. If we find the time, we will do our best to address it.

# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
