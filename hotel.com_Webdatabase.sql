CREATE DATABASE IF NOT EXISTS hotel_booking;

USE hotel_booking;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS hotels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    rating DECIMAL(2, 1) NOT NULL,
    comments INT NOT NULL,
    amenities TEXT,
    country VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    member_discount DECIMAL(3, 2),
    special_discount VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    hotel_id INT NOT NULL,
    checkin_date DATE NOT NULL,
    checkout_date DATE NOT NULL,
    guest_count INT NOT NULL,
    PRIMARY KEY (user_id, hotel_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (hotel_id) REFERENCES hotels(id)
);
INSERT INTO hotels (name, price, rating, num_comments, amenities, availability, points) VALUES
('Holiday Inn Resort Bodrum', 2.129, 8.8, 32, 'Restoran,Havuz,Klima,Bar , OtoPark,WiFi', 2, 100),
('Cana Garden Hotel -Adults Only', 821, 49.2, 348, 'Mutfak, Restaurant,Spa, Klima,Özel Çalışma alanı,özel Jakuzi', 2, 90),
('Pine Village Bungalows Ölüdeniz', 2.700, 9.4, 9, 'Poll,Wifi, Air Conditioning, Free Shuttl,OtoParke', 2, 110);
