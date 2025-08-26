<h1 align="center">gaussian-splatting-engineering</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Author-EvangelionA-orange" alt="Author" />
  <a href="./README.md"><img src="https://img.shields.io/badge/Doc-English-blue.svg" alt="ZH doc"/></a>
  <a href="docs/README_ZH.md"><img src="https://img.shields.io/badge/Doc-中文-blue.svg" alt="ZH doc"/></a>
</p>
<hr>

English | [中文](docs/README_ZH.md)

# Introduction
  This repository aims to bridge the gap between academic research and industrial deployment of 3D Gaussian Splatting (3DGS) technology. While most existing papers focus on theoretical innovations, this project emphasizes:
1. **Engineering-oriented implementation**
   
2. **Steady performance optimization**
   
3. **Systematic documentation of practical workflows**

**This project is built upon [3DGS](https://github.com/graphdeco-inria/gaussian-splatting).**

## TODO_LIST
- improvement
  - [ ] [ABS-GS](https://github.com/TY424/AbsGS)
  - [ ] [RAIN-GS](https://github.com/whuhxb/RAIN-GS)
- format support
  - [ ] [USDZ format](https://github.com/nv-tlabs/3dgrut) / [Omniverse](https://docs.nvidia.com/omniverse/index.html#get-started)
  - [ ] [SPZ format](https://github.com/nianticlabs/spz)
- doc support
  - [ ] pipeline Instructions (WIP)
  - [ ] [colmap](https://github.com/TY424/AbsGS)
    - [ ] [USER GUID]
  - [ ] [RealityCapture](https://github.com/TY424/AbsGS)
    - [ ] [USER GUID]
  - [ ] [KIRI](https://github.com/TY424/AbsGS)


# Improvement Item Description
## Improverment
 Paper | Introduction | TestResults |
 ---- | ---- | ----
 [ABS-GS](https://github.com/TY424/AbsGS) | Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification. | [result](datatest/abs-gs/)
 [RAIN-GS](https://github.com/whuhxb/RAIN-GS) | show that our simple yet effective strategy consisting of sparse-large-variance (SLV) random initialization, progressive Gaussian low-pass filter control, and the Adaptive Bound-Expanding Split (ABE-Split) algorithm robustly guides 3D Gaussians to model the scene even when starting from random point cloud. | [result](datatest/rain-gs/)

## Format Support
 format | Introduction | 
 ---- | ---- 
 [USDZ](https://github.com/nv-tlabs/3dgrut) | Universal Scene Description (USD) is a framework for interchange of 3D computer graphics data. The framework focuses on collaboration, non-destructive editing, and enabling multiple views and opinions about graphics data.
 [SPZ](https://github.com/nianticlabs/spz) | spz encoded splats are typically around 10x smaller than the corresponding .ply files, with minimal visual differences between the two. 

## Project Structure
```text
📦 gaussian-splatting-engineering
├─ 📁 docs
│  └─ README_CN.md              # 中文指南
├─ 📁 gaussian-splatting-main
│  ├─ arguments/                    
│  ├─ assets/                   
│  ├─ gaussian_renderer/                     
│  ├─ IpipsPyTorch/                    
│  ├─ scene/
│  ├─ utils/
│  ├─ .gitignore       
│  └─ README_CN.md              
├─ LICENSE
└─ README.md                    # Main overview file
```


# Gaussian-Splatting PIPELINE
## Stage_1 : Accurate Camera Pose [*Crucial*]
**bad pose bad result**

Whether it's the 3DGS project or traditional photographic surveying such as SFM, MVS, etc., the preliminary work involves obtaining sufficiently accurate camera poses. This step is crucial, as any errors in this step will directly affect the subsequent reconstruction results.

**The traditional camera pose acquisition methods include**:

openSource | commercial(free) | commercial | mobile
 ---- | ---- | ---- | ----
 [COLMAP](https://github.com/colmap/colmap) <br> (recommended) | [postshot](https://www.jawset.com/) <br> (recommended)| [ContextCapture](https://www.contextcapture.com) | [KIRI](https://www.kiri.com)
 [openMVG](https://github.com/openMVG/openMVG) | [Reality Capture](https://www.realitycapture.com) | [大疆智图](https://enterprise.dji.com/cn/dji-terra)|[Polyscam](https://www.polyscanner.com)
 [OpenSfM](https://github.com/mapillary/OpenSfM) |  | |[matterport](https://www.matterport.com)
 [MVS](https://github.com/colmap/colmap) |  | |


**feed-forward**：
 paper | Introduction | 
 ---- | ---- 
 [VGGT](https://github.com/facebookresearch/vggt) | Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification. 
 [DUST3R](https://github.com/naver/dust3r) | show that our simple yet effective strategy consisting of sparse-large-variance (SLV) random initialization, progressive Gaussian low-pass filter control, and the Adaptive Bound-Expanding Split (ABE-Split) algorithm robustly guides 3D Gaussians to model the scene even when starting from random point 
 [MAST3R](https://github.com/naver/mast3r) | Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification. 
 [FAST3R](https://github.com/facebookresearch/fast3r) | show that our simple yet effective strategy consisting of sparse-large-variance (SLV) random initialization, progressive Gaussian low-pass filter control, and the Adaptive Bound-Expanding Split (ABE-Split) algorithm robustly guides 3D Gaussians to model the scene even when starting from random point cloud.
 [etc.] |  ..
  


## Stage_2 : Gaussian Splatting Training

**software**

openSource | commercial(free) | commercial | mobile
 ---- | ---- | ---- | ----
 [COLMAP](https://github.com/colmap/colmap) <br> (recommended) | [postshot](https://www.jawset.com/) <br> (recommended)| [ContextCapture](https://www.contextcapture.com) | [KIRI](https://www.kiri.com)
 [openMVG](https://github.com/openMVG/openMVG) | [Reality Capture](https://www.realitycapture.com) | [大疆智图](https://enterprise.dji.com/cn/dji-terra)|[Polyscam](https://www.polyscanner.com)
 [OpenSfM](https://github.com/mapillary/OpenSfM) |  | |[matterport](https://www.matterport.com)
 [MVS](https://github.com/colmap/colmap) |  | |


### Getting Started

### Installing
```
pip install diff-gaussian-spaltting
```



## Stage_3 : Gaussian Splatting Application

### **VIEWER**

 Object | Introduction | UserGuide |
 ---- | ---- | ----
 [SIBR](https://sibr.gitlabpages.inria.fr/) | Official 3DGS Viewer | [gaussian-splatting-SIBR](https://github.com/graphdeco-inria/gaussian-splatting?tab=readme-ov-file#interactive-viewers)
 [SuperSplat](https://github.com/playcanvas/supersplat) <br> (**recommended**)| SuperSplat is a free and open source tool for *inspecting*, *editing*, *optimizing* and *publishing* 3D Gaussian Splats. It is built on web technologies and runs in the browser, so there's nothing to download or install. | [live version](https://superspl.at/editor)
 [LCC Viewer](https://xgrids.cn/support/download?page=LCCViewer) | Lightweight viewer for LCC models with measurement tools and annotation capabilities, optimized for project review and collaboration. | [live version](https://superspl.at/editor)
 
### **Creativefield**
 SoftWare | Object | UserGuide |
 ---- | ---- | ----
 [UE](https://sibr.gitlabpages.inria.fr/) + 3DGSPlugin | [XScene-UEPlugin](https://github.com/xverse-engine/XScene-UEPlugin/tree/main) | [gaussian-splatting-SIBR](https://github.com/graphdeco-inria/gaussian-splatting?tab=readme-ov-file#interactive-viewers)
 [Blender](https://github.com/playcanvas/supersplat) + 3DGSPlugin | [KIRI_BlenderPlugin](https://github.com/Kiri-Innovation/3dgs-render-blender-addon) <br> [mediastormDev-BlenderNode](https://github.com/mediastormDev/Blender-3DGS-4DGS-Viewer-Node)| 



### **Production**
 Object | Introduction | UserGuide |
 ---- | ---- | ----
 [Omniverse](https://docs.nvidia.com/omniverse/index.html#get-started) | Official 3DGS Viewer | [gaussian-splatting-SIBR](https://github.com/graphdeco-inria/gaussian-splatting?tab=readme-ov-file#interactive-viewers)
 [Blender](https://www.blender.org/) | SuperSplat is a free and open source tool for *inspecting*, *editing*, *optimizing* and *publishing* 3D Gaussian Splats. It is built on web technologies and runs in the browser, so there's nothing to download or install. | [live version](https://superspl.at/editor)

## FAQ

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

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Acknowledgments

This project is built upon [3DGS](https://github.com/graphdeco-inria/gaussian-splatting).  We thank all the authors for their great repos.
