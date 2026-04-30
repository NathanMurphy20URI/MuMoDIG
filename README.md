# Multiple Monotonic Diversified Integrated Gradients (MuMoDIG)
Final Project for CSC492 at URI.  

This code is from the 2025 AAAI Conference Paper ["Improving Integrated Gradient-based Transferable Adversarial Examples by Refining the Integration Path"](https://ojs.aaai.org/index.php/AAAI/article/view/32722).   
Original attack code for this paper is sourced at [a Github located here](https://github.com/RYC-98/MuMoDIG/tree/main).  

This code allows for generating transferable adversarial examples against a range of CNN and Vision Transformer (ViT) surrogate models, including ResNet-18, DenseNet-121, EfficientNet-B0, MobileNet-V3, DeiT, PiT, CoaT, and Swin Transformer.  
All attacks are implemented using PyTorch and evaluated on ImageNet-compatible input pipelines.  
Supported attack algorithms (via --attack) include MuMoDIG, MuMoDIG-PNA, and MuMoDIG-SGM, with optional ensemble attacks across multiple surrogate models.  
Each attack can be run from the command line by specifying the desired algorithm, source model, epsilon budget, and input/output directories. Untargeted and targeted attack modes are both supported.  
Attack success rate (ASR) is evaluated across a suite of pretrained CNN and ViT models using the --eval flag.
# Step by Step Guide
<ol>
  <li>Install the packages listed in the Software Installation Section (see below).</li>
  <li>Download the github codebase.
  <li>Run the "get_vit_weights.py" file. This pulls weights from timm and places them in the vit_weight folder.</li>
  <li>Open the project and main.py file in the Python IDE of your choice. Run the main.py file to generate adversarials</li>
  <li>Use the -e flag to evaluate the adversarials. </li>  
  <li>Generate adversarials and evaluate them using different flags, listed in the file.</li>
</ol>

# Software Installation
Python >= 3.6  
PyTorch >= 1.12.1  
Torchvision >= 0.13.1  
timm >= 0.6.12  
tqdm   
pandas  
scikit-optimize  
matplotlib  
kornia  

# Models
This attack supports both CNN and Vision Transformer (ViT) surrogate models:  

CNNs: ResNet-18 (default), DenseNet-121, EfficientNet-B0, MobileNet-V3-Small   


ViTs: DeiT-Tiny (deit_tiny_patch16_224), PiT-Ti (pit_ti_224), CoaT-Tiny (coat_tiny), Swin-Tiny (swin_tiny_patch4_window7_224)  
ViT's may be obtained using the get_vit_weights.py file mentioned above.

For ensemble attacks, the default surrogate set is: ResNet-18, EfficientNet-B0, MobileNet-V3-Small, DeiT-Tiny, PiT-Ti, and Swin-Small.

# System Requirements
Internet Connection Required. Cuda-compatible GPU Recommended. All attacks were tested on Windows 11 using a NVIDIA Geforce RTX 4060 Laptop GPU, and 12GB of RAM. Recommended 20+ GB of Storage. Ensemble attack recommends a larger amount of RAM for speed purposes.

# Contact
All followup questions and inquiries may be sent to nathanmurphy20@uri.edu 
