# 🛡️ Criminal Identification & Tracking System using Face Recognition

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-darkgreen.svg)](https://www.djangoproject.com/)
[![DeepFace](https://img.shields.io/badge/AI-DeepFace-orange.svg)](https://github.com/serengil/deepface)
[![OpenCV](https://img.shields.io/badge/Computer%20Vision-OpenCV-red.svg)](https://opencv.org/)
[![Platform](https://img.shields.io/badge/Deployed-Render-brightgreen.svg)](https://render.com/)

An automated web-based security and surveillance platform designed to identify and track criminals using facial recognition technologies. Built with **Django**, **DeepFace**, **OpenCV**, and **TensorFlow**, this system streamlines record management for police departments and accelerates suspect identification in real time.

---

## 📌 Table of Contents
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Project Directory Structure](#-project-directory-structure)
- [Installation & Local Setup](#-installation--local-setup)
- [Deployment (Render)](#-deployment-render)
- [API & Route Overview](#-api--route-overview)
- [License](#-license)

---

## 🚀 Key Features

* **Facial Recognition & Match Validation:** Utilizes pre-trained deep learning representations (`DeepFace`, `RetinaFace`, and `MTCNN`) to cross-reference suspect photos against criminal databases.
* **Role-Based Access Control:** Separate portals and dashboard experiences for Administrative Officers and Law Enforcement Users.
* **Criminal Record Management:** Add, update, search, and view detailed criminal profiles, history, and associated crime records.
* **Police Station & Officer Administration:** Maintain station listings, assign officer responsibilities, and manage access privileges.
* **Automated Identity Verification:** Quick lookup pipelines to search suspects via uploaded surveillance captures and match score thresholds.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.10, Django 4.2
* **Computer Vision & Deep Learning:** DeepFace, OpenCV (Headless), TensorFlow, Keras, MTCNN, RetinaFace
* **Data Processing & Scientific Computing:** NumPy, Pandas, Pillow, SciPy
* **Database:** SQLite (Default / Local / Render Cloud) / MySQL Compatible
* **Static Assets & Server:** Gunicorn, WhiteNoise

---

## 📂 Project Directory Structure

```text
face-detection-criminal-identification-system/
│
├── .python-version               # Pinned Python version (3.10.14)
├── ABSTRACT/                     # Project abstract documents
├── CERTIFICATION.docx            # Certification docs
├── DOCUMENTATION.docx            # Technical documentation
├── Mini Project ppt.pptx         # Presentation deck
├── README.md                     # Project documentation
│
└── SOURCE CODE/                  # Core Application Directory
    ├── manage.py
    ├── requirments.txt           # Dependency specifications
    ├── db.sqlite3                # SQLite database file
    │
    ├── Criminal_Tracker_Face_Detection/  # Main Django project configuration
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├── adminapp/                 # Admin operations & officer management
    ├── homeapp/                  # Public landing, information & auth views
    ├── userapp/                  # Officer/Investigator search & verification views
    │
    ├── assets/                   # Static assets (CSS, JS, images, templates)
    └── media/                    # Stored suspect images and uploads
