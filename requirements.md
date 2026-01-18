# 🚗 AI-Based Smart Parking Detection & Automated Billing System

## 1. Overview

This project proposes a **camera-based intelligent parking system** that uses **computer vision (YOLO)** to detect parking slot availability in real time and automatically generates **time-based parking tickets** with **exit-based billing**.

The system eliminates physical sensors, reduces manual intervention, and enables **smart, scalable parking management** using only cameras and cloud services.

---

## 2. Problem Statement

Urban parking systems suffer from:

- Time wasted searching for parking slots
- Manual ticketing and billing at exits
- Inefficient utilization of parking spaces
- High infrastructure cost using physical sensors

Existing systems lack **real-time intelligence** and **automation**.

---

## 3. Proposed Solution

A fully automated parking system that:

- Detects **occupied and free parking slots** using YOLO
- Allows users to **generate a parking ticket digitally**
- Tracks parking duration automatically
- Calculates parking charges at exit using **vehicle number recognition**
- Supports **online payment** and automatic slot release

---

## 4. Key Features

- Real-time parking slot detection
- Digital ticket generation with timestamp
- Slot-to-vehicle assignment
- Automatic billing based on parking duration
- Camera-only setup (no IoT sensors)
- Cloud-hosted and scalable

---

## 5. User Flow

### 5.1 Entry / Parking

1. CCTV camera monitors the parking area
2. YOLO model detects vehicles
3. System identifies **free parking slots**
4. User opens the web UI
5. User clicks **Generate Ticket**
6. System assigns:
   - Slot ID
   - Entry timestamp
   - Vehicle number

---

### 5.2 Parking Monitoring

1. YOLO continuously monitors the assigned slot
2. Slot status remains **occupied** while vehicle is present
3. When the vehicle leaves the slot:
   - Slot is marked **free**
   - Parking session continues until exit

---

### 5.3 Exit & Billing

1. Exit camera captures vehicle image
2. Vehicle number is extracted using OCR
3. System fetches the active ticket
4. Parking duration is calculated:

# 🚗 AI-Based Smart Parking Detection & Automated Billing System

## 1. Overview

This project proposes a **camera-based intelligent parking system** that uses **computer vision (YOLO)** to detect parking slot availability in real time and automatically generates **time-based parking tickets** with **exit-based billing**.

The system eliminates physical sensors, reduces manual intervention, and enables **smart, scalable parking management** using only cameras and cloud services.

---

## 2. Problem Statement

Urban parking systems suffer from:

- Time wasted searching for parking slots
- Manual ticketing and billing at exits
- Inefficient utilization of parking spaces
- High infrastructure cost using physical sensors

Existing systems lack **real-time intelligence** and **automation**.

---

## 3. Proposed Solution

A fully automated parking system that:

- Detects **occupied and free parking slots** using YOLO
- Allows users to **generate a parking ticket digitally**
- Tracks parking duration automatically
- Calculates parking charges at exit using **vehicle number recognition**
- Supports **online payment** and automatic slot release

---

## 4. Key Features

- Real-time parking slot detection
- Digital ticket generation with timestamp
- Slot-to-vehicle assignment
- Automatic billing based on parking duration
- Camera-only setup (no IoT sensors)
- Cloud-hosted and scalable

---

## 5. User Flow

### 5.1 Entry / Parking

1. CCTV camera monitors the parking area
2. YOLO model detects vehicles
3. System identifies **free parking slots**
4. User opens the web UI
5. User clicks **Generate Ticket**
6. System assigns:
   - Slot ID
   - Entry timestamp
   - Vehicle number

---

### 5.2 Parking Monitoring

1. YOLO continuously monitors the assigned slot
2. Slot status remains **occupied** while vehicle is present
3. When the vehicle leaves the slot:
   - Slot is marked **free**
   - Parking session continues until exit

---

### 5.3 Exit & Billing

1. Exit camera captures vehicle image
2. Vehicle number is extracted using OCR
3. System fetches the active ticket
4. Parking duration is calculated:
