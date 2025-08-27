<h1 align="center">gaussian-splatting-engineering</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Author-EvangelionA-orange" alt="Author" />
  <a href="./README.md"><img src="https://img.shields.io/badge/Doc-English-blue.svg" alt="ZH doc"/></a>
  <a href="docs/README_CN.md"><img src="https://img.shields.io/badge/Doc-中文WIP-blue.svg" alt="ZH doc"/></a>
</p>
<hr>

English | [中文-WIP](docs/README_CN.md)

# Introduction
  This repository aims to bridge the gap between academic research and industrial deployment of 3D Gaussian Splatting (3DGS) technology. While most existing papers focus on theoretical innovations, this project emphasizes:
1. **Engineering-oriented implementation**
   
2. **Steady performance optimization**
   
3. **Systematic documentation of practical workflows**

**This project is built upon [3DGS](https://github.com/graphdeco-inria/gaussian-splatting).**

## TODO_LIST
- **improvement**
  - [ ] [ABS-GS](https://github.com/TY424/AbsGS)
  - [ ] [RAIN-GS](https://github.com/whuhxb/RAIN-GS)
  - [ ] **......**
- **format support**
  - [ ] [USDZ format](https://github.com/nv-tlabs/3dgrut) / [Omniverse](https://docs.nvidia.com/omniverse/index.html#get-started)
  - [ ] [SPZ format](https://github.com/nianticlabs/spz)
- **doc support**
  - [ ] pipeline Instructions (WIP)
  - [ ] [colmap](https://github.com/TY424/AbsGS)
    - [ ] [USER GUID]
  - [ ] [RealityCapture](https://github.com/TY424/AbsGS)
    - [ ] [USER GUID]
  - [ ] [KIRI](https://github.com/TY424/AbsGS)
  - [ ] **......**
- **release package**
  - [x] v0.0.0 (3DGS-baseline)
  - [x] Google Drive
  - [x] Baidu Disk


# Improvement Item Description
## Improverment
 Paper | Introduction | TestResults |
 ---- | ---- | ----
 [ABS-GS](https://github.com/TY424/AbsGS) | Reveal that the original adaptive density control strategy in 3D Gaussian Splatting (3D-GS) has the flaw of gradient collision which results in degradation, and propose homodirectional gradient as the guidance for densification. | [result-WIP](dataTestResult/abs-gs/)
 [RAIN-GS](https://github.com/whuhxb/RAIN-GS) | show that our simple yet effective strategy consisting of sparse-large-variance (SLV) random initialization, progressive Gaussian low-pass filter control, and the Adaptive Bound-Expanding Split (ABE-Split) algorithm robustly guides 3D Gaussians to model the scene even when starting from random point cloud. | [result-WIP](dataTestResult/rain-gs/)
 etc. | **......**

## Format Support
 format | Introduction | 
 ---- | ---- 
 [USDZ](https://github.com/nv-tlabs/3dgrut) | Universal Scene Description (USD) is a framework for interchange of 3D computer graphics data. The framework focuses on collaboration, non-destructive editing, and enabling multiple views and opinions about graphics data.
 [SPZ](https://github.com/nianticlabs/spz) | spz encoded splats are typically around 10x smaller than the corresponding .ply files, with minimal visual differences between the two. 

## Project Structure
```text
📦 gaussian-splatting-engineering
├─ 📁 dataTestResult
├─ 📁 docs
│  └─ README_CN.md              
├─ 📁 gaussian-splatting-main
│  ├─ arguments/                    
│  ├─ assets/                   
│  ├─ gaussian_renderer/                     
│  ├─ IpipsPyTorch/                    
│  ├─ scene/
│  ├─ SIBR_viewers/
│  ├─ submodules/
│  ├─ utils/
│  ├─ .gitignore
│  ├─ .gitmodules
│  ├─ convert.py
│  ├─ environment.yml
│  ├─ full_eval.py
│  ├─ LICENSE.md
│  ├─ metrics.py
│  ├─ README.md
│  ├─ render.py
│  ├─ results.py
│  └─ train.py        
├─ LICENSE
└─ README.md                    
```


# Gaussian-Splatting PIPELINE
## Stage_1 : Accurate Camera Pose [*Crucial*]
**!!! bad pose bad result**

Whether it's the 3DGS project or traditional photographic surveying such as SFM, MVS, etc., the preliminary work involves obtaining sufficiently accurate camera poses. This step is crucial, as any errors in this step will directly affect the subsequent reconstruction results.

**The traditional camera pose acquisition methods and 3D Reconstruction APP include**:

openSource | commercial(free) | commercial | mobile
 ---- | ---- | ---- | ----
 [COLMAP](https://github.com/colmap/colmap) <br> (recommended) | [postshot](https://www.jawset.com/) <br> (recommended)| [ContextCapture](https://www.bentley.cn/software/reality-and-spatial-modeling/) | [KIRI Engine](https://www.kiriengine.app/)
 [OpenSFM](https://github.com/mapillary/OpenSfM) | [RealityScan / RealityCapture](https://www.realityscan.com/en-US) | [DJI TERRA](https://enterprise.dji.com/cn/dji-terra) | [Polycam](https://poly.cam/)
 [openMVS](https://github.com/cdcseacave/openMVS) |  | [matterport](https://matterport.com/?srsltid=AfmBOor0O6mOJot6qlPXNSAimFjW-oLNI4x7l3ePkJ2vtatHGmB9vhJ6)|[RealityScan](https://www.realityscan.com/en-US)
 [openMVG](https://github.com/openMVG/openMVG) |  | |[matterport](https://matterport.com/?srsltid=AfmBOor0O6mOJot6qlPXNSAimFjW-oLNI4x7l3ePkJ2vtatHGmB9vhJ6)


**FEED-FORWARD**：
 paper | Introduction | 
 ---- | ---- 
 [VGGT](https://github.com/facebookresearch/vggt) | Visual Geometry Grounded Transformer (VGGT, CVPR 2025) is a feed-forward neural network that directly infers all key 3D attributes of a scene, including extrinsic and intrinsic camera parameters, point maps, depth maps, and 3D point tracks, from one, a few, or hundreds of its views, within seconds.
 [DUST3R](https://github.com/naver/dust3r) | This paper introduces DUSt3R, a novel approach for dense 3D reconstruction from arbitrary image collections without requiring prior camera calibration or pose information. It formulates pairwise reconstruction as a regression of pointmaps, unifying monocular and binocular cases. For multi-image inputs, a global alignment strategy aligns pairwise pointmaps into a common frame. Built on Transformer encoders/decoders, DUSt3R directly produces 3D models and depth maps while enabling recovery of pixel matches and camera parameters. Experiments demonstrate state-of-the-art performance across monocular/multi-view depth estimation and relative pose estimation tasks.
 [MAST3R](https://github.com/naver/mast3r) | MASt3R(1) brings a new level of precision and detail to 3D reconstruction and localization tasks by providing pixel correspondences for even very large image collections. The remarkable results of MASt3R are achieved by adding an extra head to the DUSt3R framework(2) and a matching algorithm so that it efficiently outputs a 3D reconstruction that is metric along with dense local feature maps, providing accurate depth perception and spatial understanding.
 [FAST3R](https://github.com/facebookresearch/fast3r) | In this work, propose Fast 3D Reconstruction (Fast3R), a novel multi-view generalization to DUSt3R that achieves efficient and scalable 3D reconstruction by processing many views in parallel. Fast3R's Transformer-based architecture forwards N images in a single forward pass, bypassing the need for iterative alignment. 
 etc. |  **......**
  


## Stage_2 : Gaussian Splatting Training(WIP)

**software(incomplete)**
 commercial(free) | mobile | 
 ---- | ---- 
[postshot](https://www.jawset.com/) <br> (recommended) | [KIRI Engine](https://www.kiriengine.app/)
[DJI TERRA](https://enterprise.dji.com/cn/dji-terra) | [Polycam](https://poly.cam/)




### Getting Started

### Installing

reference [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting#setup)



## Stage_3 : Gaussian Splatting Application

### **VIEWER**

 Object | Introduction | UserGuide |
 ---- | ---- | ----
 [SIBR](https://sibr.gitlabpages.inria.fr/) | Official 3DGS Viewer | [gaussian-splatting-SIBR](https://github.com/graphdeco-inria/gaussian-splatting?tab=readme-ov-file#interactive-viewers)
 [SuperSplat](https://github.com/playcanvas/supersplat) <br> (**recommended**)| SuperSplat is a free and open source tool for *inspecting*, *editing*, *optimizing* and *publishing* 3D Gaussian Splats. It is built on web technologies and runs in the browser, so there's nothing to download or install. | [live version](https://superspl.at/editor)
 [LCC Viewer](https://xgrids.cn/support/download?page=LCCViewer) | Lightweight viewer for LCC models with measurement tools and annotation capabilities, optimized for project review and collaboration. | [website](https://xgrids.com/support/download?page=LCCViewer)
 
### **Creativefield**
 SoftWare | Object | Introduction |
 ---- | ---- | ----
 [UE](https://sibr.gitlabpages.inria.fr/) + 3DGSPlugin | [XScene-UEPlugin](https://github.com/xverse-engine/XScene-UEPlugin/tree/main) | It provides real-time visualization, management, editing, and scalable hybrid rendering of Gaussian Splatting models—a novel technique for reconstructing 3D scenes from multi-view photos. 
 [Blender](https://github.com/playcanvas/supersplat) + 3DGSPlugin | [KIRI_BlenderPlugin](https://github.com/Kiri-Innovation/3dgs-render-blender-addon) <br> | 1.Work with 3DGS content in a familiar environment.<br>2.Edit and optimize point clouds before 3DGS conversion.<br> 3.Create animations and motion graphics.<br>4.Objects react to lighting and cast shadows|
 [Blender](https://github.com/playcanvas/supersplat) + 3DGS +4DG ViewerNode |[mediastormDev-BlenderNode](https://github.com/mediastormDev/Blender-3DGS-4DGS-Viewer-Node) | A custom Blender node developed by Mediastorm during the ASUS 4DGS Yungang Grottoes project. Supports loading and previewing of 3DGS and 4DGS datasets, with basic rendering styles for quick inspection.
 etc. |  **......**
 



### **Production**
 Object | Introduction | UserGuide |
 ---- | ---- | ----
 [Omniverse](https://docs.nvidia.com/omniverse/index.html#get-started) | NVIDIA Omniverse is a platform of APIs, Services, and Software Development Kits (SDKs) that enable developers to build generative AI-enabled﻿ tools, applications, and services for industrial digitalization. | [SDK](https://docs.nvidia.com/omniverse/index.html#get-started)
 [NVIDIA Isaac](https://developer.nvidia.com/isaac) | Ready to jump start your AI robot development? The NVIDIA Isaac™ platform delivers the NVIDIA® CUDA®-accelerated libraries, application frameworks, and AI models you need to create autonomous mobile robots (AMRs), arms and manipulators, humanoids, and more. | [github](https://github.com/nvidia-isaac) |
 [OpenUSD](https://developer.nvidia.com/usd?sortBy=developer_learning_library%2Fsort%2Ffeatured_in.usd_resources%3Adesc%2Ctitle%3Aasc&hitsPerPage=6) | Developed by Pixar Animation Studios, OpenUSD is an open-source framework for creating, simulating, and collaborating in 3D worlds. OpenUSD is foundational to NVIDIA Omniverse™, the platform for developing 3D applications for industrial digitalization and generative physical AI. | [DOC](https://developer.nvidia.com/usd?sortBy=developer_learning_library%2Fsort%2Ffeatured_in.usd_resources%3Adesc%2Ctitle%3Aasc&hitsPerPage=6#section-getting-started)
  etc. |  **......**

## Acknowledgments

This project is built upon [3DGS](https://github.com/graphdeco-inria/gaussian-splatting).  We thank all the authors for their great repos.

## Contributing

Thank you very much for the contribution of the 3DGS project to the open source community!

<section class="section" id="BibTeX">
  <div class="container is-max-desktop content">
    <h3 class="title">BibTeX</h3>
    <pre><code>@Article{kerbl3Dgaussians,
      author       = {Kerbl, Bernhard and Kopanas, Georgios and Leimk{\"u}hler, Thomas and Drettakis, George},
      title        = {3D Gaussian Splatting for Real-Time Radiance Field Rendering},
      journal      = {ACM Transactions on Graphics},
      number       = {4},
      volume       = {42},
      month        = {July},
      year         = {2023},
      url          = {https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/}
}</code></pre>
  </div>
</section>

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details