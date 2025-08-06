# Generative Artificial Intelligence University Projects

This repository contains the implementation and results of projects completed for the **“Generative Artificial Intelligence”** course at the Technical University of Crete. The coursework is split into two major projects, each emphasizing the latest generative techniques in 3D shape modeling and image generation.

---

## 📚 Project Overview

The repository includes **two projects** focusing on advanced neural and generative modeling for both 3D reconstruction and image synthesis. Each project is summarized below:

### **Project 1: Implicit 3D Surface Generation**

In this assignment, you will generate 3D shape surfaces conditioned on sparse point clouds, implementing both classical geometric and modern neural approaches.

#### **Tasks and Methods**
1. **Geometric Signed Distance Function**  
   - Implement a function to measure the signed distance from any 3D grid point to the tangent plane of the nearest surface point in a given point cloud.
   - This is realized in `naiveReconstruction.py`.

2. **Neural Signed Distance Function**  
   - Design and train a multi-layer fully connected neural network that approximates the signed distance field (SDF) for the given 3D data.  
   - The architecture consists of 8 fully connected layers with weight normalization, leaky ReLU activations, dropout, dimensional concatenation, and a final tanh output.
   - Code is completed in `model.py` and `neuralNetReconstruction.py`, following a provided starter template.

---

### **Project 2: Denoising Diffusion Probabilistic Models (DDPM)**

This programming assignment explores the implementation of DDPMs, foundational to state-of-the-art generative models like Stable Diffusion.

#### **Tasks and Components**
1. **2D Swiss Roll (Toy Example)**
   - Implement a custom noise prediction network and the DDPM forward/reverse processes for 2D point clouds in `2d_plot_diffusion_todo/`.
   - Build the training loss and iterate until the model can synthesize samples similar to the target 2D distribution.

2. **Image Generation with AFHQ Dataset**
   - Implement the `add_noise` and `step` functions for the scheduler, and `get_loss` in the diffusion model.
   - Train a DDPM capable of generating novel 64x64 animal images after several hours of training.

3. **Evaluation**
   - Include loss curves, Chamfer Distance scores, and images visualizing samples for the 2D Swiss Roll experiment.
   - For image diffusion, measure the FID score on the validation set and present at least 8 generated images.

---
