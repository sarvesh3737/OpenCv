# Parking Lot Management System

A robust and extensible command-line application for managing a small parking lot.
Users can specify the total number of slots and manage entry, exit, and status of vehicles of various sizes.
*All data is stored in memory—no database required!*

---

## 🚗 Features

* **User-defined Slots:** Initialize the parking lot with any number of slots.
* **Slot Size Classification:** Three slot types — Small, Large, Oversize.
* **Vehicle Management:** Park, unpark, and locate vehicles by license plate.
* **Duplicate Prevention:** License plates must be unique within the lot.
* **Real-time Status:** View slot availability for each slot size.
* **Input Validation & Error Handling:** Handles invalid/duplicate entries gracefully.
* **Extensible:** Easily add more vehicle or slot types if needed.

---

## 🏗️ Approach & Design

### Object-Oriented Structure

* **Classes:**

  * `ParkingLot`: Singleton class managing all slots and operations.
  * `ParkingSpot`: Represents a single slot, tracks its type and occupancy.
  * `Vehicle` (abstract) and its subclasses: `SmallCar`, `LargeCar`, `SUV`, `Truck`.
  * Enums for vehicle/slot types for type-safety and clarity.
* **Initialization Logic:**

  * User specifies number of slots (`n`).
  * Slots are divided approximately as: 50% Small, 33% Large, rest Oversize (minimum 1 of each type).

---

## 🗂️ File Structure

```
parkinglot/
│
├── parking_lot_interactive.py   # Main CLI application (entry point)
├── parking_lot.py               # ParkingLot core logic
├── parking_spot.py              # ParkingSpot class
├── vehicle.py                   # Abstract Vehicle base class
├── car.py                       # SmallCar, LargeCar, SUV, Truck classes
├── vehicle_type.py              # Enums: VehicleType, SlotSize
├── README.md                    # Project documentation
└── info.txt                     # Project requirements/specs
```

---

## ▶️ How to Run

### Requirements

* Python 3.7 or higher

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

3. **Follow on-screen prompts to park/unpark vehicles or view status.**

---

## 💡 Example Usage

```
Welcome to Parking Lot Management System!
Enter the total number of parking slots (n): 8

Parking lot initialized with 8 slots:
  Small slots: 4
  Large slots: 2
  Oversize slots: 2

=== PARKING LOT MANAGEMENT SYSTEM ===
1. Park a vehicle
2. Unpark a vehicle
3. Display availability
4. Exit
=====================================
Enter your choice (1-4): 1

Select vehicle type:
1. Small Car
2. Large Car
3. SUV
4. Truck
Enter your choice (1-4): 3
Enter license plate: ABC123

Vehicle ABC123 parked successfully in spot 6
```

---

## 🧪 Test Data

* The application is interactive and does not require pre-loaded data.
* You can add/remove vehicles via CLI and observe how slots fill up or become available.
* *(Optional: For automated testing or demonstrations, you can script a series of actions in a Python file.)*

---

## 📋 Assumptions & Design Decisions

* At least one slot of each type (Small, Large, Oversize) if possible.
* Vehicles can only park in slots of matching size (no upgrades/downgrades).
* License plates must be unique, 3–10 characters, alphanumeric.
* All data is lost upon program exit (in-memory only).
* Maximum supported slots: 10,000.

---

## 🧩 Extensibility

* New vehicle/slot types can be added by extending classes/enums.
* The design supports adding persistence or a graphical interface with minimal code changes.

---

## 👨‍💻 Key Classes

* **ParkingLot:** Manages all slots and vehicles; singleton pattern.
* **ParkingSpot:** Represents an individual slot and its state.
* **Vehicle:** Abstract class; implemented by `SmallCar`, `LargeCar`, `SUV`, `Truck`.
* **Enums:** For clear, type-safe representation of vehicle and slot types.

---

## 🏷️ License

MIT (or specify your license here).

---

## 📞 Contact

For questions, contact \[[your-email@example.com](mailto:your-email@example.com)] or open an issue on this repository.

---

*This README is ready for submission and professional use!*
