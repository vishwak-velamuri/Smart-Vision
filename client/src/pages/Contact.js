import React, { useState } from 'react';

const Contact = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Logic to handle form submission
        console.log('Form submitted:', formData);
    };

    return (
        <div className="contact">
            <h1>Contact Us</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Name:
                    <input type="text" name="name" value={formData.name} onChange={handleChange} required />
                </label>
                <label>
                    Email:
                    <input type="email" name="email" value={formData.email} onChange={handleChange} required />
                </label>
                <label>
                    Message:
                    <textarea name="message" value={formData.message} onChange={handleChange} required></textarea>
                </label>
                <button type="submit">Send</button>
            </form>

            <h2>Other Contacts</h2>
            <div className="contact-info">
                <h3>Venkata Vishwaksena Velamuri</h3>
                <p>Email: vishwaksena.velamuri@gmail.com</p>
                <p>Phone: (919) 995-2889</p>
            </div>
            <div className="contact-info">
                <h3>Tejjas Kaul</h3>
                <p>Email: tejjas15@gmail.com</p>
                <p>Phone: (919) 627-3627</p>
            </div>
        </div>
    );
};

export default Contact;