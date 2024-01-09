# North Pole API

This repository contains a FastAPI-based API for managing elves and packages at the North Pole. It utilizes SQLite as a database to store information about elves and their assigned packages.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- [FastAPI](https://fastapi.tiangolo.com/)
- SQLite3

### Dependecies

```bash 
pip3 install "uvicorn[standard]" fastapi
```

### How to run: 

```bash
uvicorn app.main:app --reload
```


## Endpoints

### 1. Get All Parcels

- **Endpoint:** `/parcels`
- **Method:** `GET`
- **Description:** Retrieve information about all parcels.
- **Response:**
  - Success: Status 200 OK with parcel data.
  - Error: Status 404 Not Found if no parcels are available.

### 2. Get All Elves

- **Endpoint:** `/elves/all`
- **Method:** `GET`
- **Description:** Retrieve information about all elves.
- **Response:**
  - Success: Status 200 OK with elf data.
  - Error: Status 404 Not Found if no elves are available.

### 3. Post Parcel

- **Endpoint:** `/parcel`
- **Method:** `POST`
- **Description:** Add a new parcel.
- **Request Body:**
  - `name` (string): Name of the parcel.
  - `elfID` (integer): ID of the assigned elf.
- **Response:**
  - Success: Status 200 OK with a success message.

### 4. Put Parcel

- **Endpoint:** `/parcel`
- **Method:** `PUT`
- **Description:** Update the status of a parcel.
- **Request Body:**
  - `parcel_id` (integer): ID of the parcel to update.
  - `status` (boolean): New status of the parcel.
- **Response:**
  - Success: Status 200 OK with a success message.

### 5. Get Parcel

- **Endpoint:** `/parcel`
- **Method:** `GET`
- **Description:** Get information about a specific parcel.
- **Query Parameter:**
  - `parcel_id` (integer): ID of the parcel to retrieve.
- **Response:**
  - Success: Status 200 OK with parcel data.
  - Error: Status 404 Not Found if no parcel with the given ID.

### 6. Delete Parcel

- **Endpoint:** `/parcels/{parcel_id}`
- **Method:** `DELETE`
- **Description:** Delete a parcel by ID.
- **Path Parameter:**
  - `parcel_id` (integer): ID of the parcel to delete.
- **Response:**
  - Success: Status 200 OK with a success message.

### 7. Post Elf

- **Endpoint:** `/elves`
- **Method:** `POST`
- **Description:** Add a new elf.
- **Request Body:**
  - `elf_name` (string): Name of the elf.
- **Response:**
  - Success: Status 200 OK with a success message.

### 8. Put Elf

- **Endpoint:** `/elves`
- **Method:** `PUT`
- **Description:** Update elf information.
- **Request Body:**
  - `elfID` (integer): ID of the elf to update.
  - `vacation` (boolean): Elf's vacation status.
  - `daternity` (boolean): Elf's paternity leave status.
- **Response:**
  - Success: Status 200 OK with a success message.

### 9. Get Elf

- **Endpoint:** `/elves`
- **Method:** `GET`
- **Description:** Get information about a specific elf.
- **Query Parameter:**
  - `elfID` (integer): ID of the elf to retrieve.
- **Response:**
  - Success: Status 200 OK with elf data.
  - Error: Status 404 Not Found if no elf with the given ID.

### 10. Delete Elf

- **Endpoint:** `/elves`
- **Method:** `DELETE`
- **Description:** Fire an elf by ID.
- **Query Parameter:**
  - `elfID` (integer): ID of the elf to fire.
- **Response:**
  - Success: Status 200 OK with a success message.

## Database Tables

### Parcels Table

- **Columns:**
  - `id` (integer): Parcel ID (Primary Key, Autoincrement)
  - `elfID` (integer): ID of the assigned elf.
  - `name` (text): Name of the parcel.
  - `status` (integer): Status of the parcel (default: 0).

### Elves Table

- **Columns:**
  - `id` (integer): Elf ID (Primary Key, Autoincrement)
  - `name` (text): Name of the elf.
  - `vacation` (integer): Vacation status of the elf (default: 0).
  - `daternity` (integer): Paternity leave status of the elf (default: 0).
