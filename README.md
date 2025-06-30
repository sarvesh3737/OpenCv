# Parking Lot Management System

A robust and extensible command-line application for managing a small parking lot.  
Users can specify the total number of slots and manage entry, exit, and status of vehicles of various sizes.  
_All data is stored in memory—no database required!_

---

## Features

- **User-defined Slots:** Initialize the parking lot with any number of slots.
- **Slot Size Classification:** Three slot types — Small, Large, Oversize.
- **Vehicle Management:** Park, unpark, and locate vehicles by license plate.
- **Duplicate Prevention:** License plates must be unique within the lot.
- **Real-time Status:** View slot availability for each slot size.
- **Input Validation & Error Handling:** Handles invalid/duplicate entries gracefully.
- **Extensible:** Easily add more vehicle or slot types if needed.

---

## Approach & Design

### Object-Oriented Structure

- **Classes:**  
  - `ParkingLot`: Singleton class managing all slots and operations.
  - `ParkingSpot`: Represents a single slot, tracks its type and occupancy.
  - `Vehicle` (abstract) and its subclasses: `SmallCar`, `LargeCar`, `SUV`, `Truck`.
  - Enums for vehicle/slot types for type-safety and clarity.

## 🗂️ File Structure



## ▶️ How to Run

### Requirements

- Python 3.7 or higher

### Steps

1. **Clone the repo:**
    ```sh
    git clone <your-github-repo-url>
    cd parkinglot
    ```

2. **Run the application:**
    ```sh
    python parking_lot_interactive.py
    ```


---

---

## 📋 Assumptions & Design Decisions

- At least one slot of each type (Small, Large, Oversize) if possible.
- Vehicles can only park in slots of matching size (no upgrades/downgrades).
- License plates must be unique, 3–10 characters, alphanumeric.
- All data is lost upon program exit (in-memory only).
- Maximum supported slots: 10,000.

---

---

## Key Classes

- **ParkingLot:** Manages all slots and vehicles; singleton pattern.
- **ParkingSpot:** Represents an individual slot and its state.
- **Vehicle:** Abstract class; implemented by `SmallCar`, `LargeCar`, `SUV`, `Truck`.
- **Enums:** For clear, type-safe representation of vehicle and slot types.




