# lateshow-heeran-yazeed

This is a REST API for managing Late Show guest appearances built with Flask, SQLAlchemy, and Flask-Migrate. It models episodes, guests, and their appearances on the show.

---

## 📦 Features

* View all episodes
* View a specific episode with all guest appearances
* View all guests
* Add a new guest appearance
* Data validations (e.g. rating must be between 1 and 5)
* Cascade deletes on episodes and guests
* Database seeding from CSV

---

## 🏁 Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:Brigid2191/lateshow-heeran-yazeed.git
cd lateshow-heeran-yazeed
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🛠️ Run the App

```bash
python run.py
```

The app will be available at: `http://127.0.0.1:5000`

---

## 🔁 API Endpoints

### GET `/episodes`

Returns all episodes.

### GET `/episodes/<id>`

Returns one episode with guest appearances.

#### Example:

```json
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "rating": 4,
      "guest_id": 1,
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      }
    }
  ]
}
```

### GET `/guests`

Returns all guests.

### POST `/appearances`

Creates a new appearance.

#### Request Body:

```json
{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 3
}
```

#### Successful Response:

```json
{
  "id": 10,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}
```

#### Error Response:

```json
{
  "errors": ["Rating must be between 1 and 5"]
}
```

---

## 🧪 Testing with Postman

1. Open Postman
2. Click `Import`
3. Upload `challenge-4-lateshow.postman_collection.json` from the project directory
4. Test all endpoints with sample data

---

## 🧬 Seeding the Database

Make sure your database is migrated, then:

```bash
flask shell
```

```python
from app.seed import seed_data
seed_data()
```

---

## 📄 Requirements

* Flask
* Flask-SQLAlchemy
* Flask-Migrate

Install with:

```bash
pip install -r requirements.txt 
```
