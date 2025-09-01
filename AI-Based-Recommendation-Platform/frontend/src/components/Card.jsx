import React from 'react';

const Card = ({ item }) => {
    return (
        <div className="card">
            <img src={item.imageUrl} alt={item.title} className="card-image" />
            <div className="card-content">
                <h3 className="card-title">{item.title}</h3>
                <p className="card-description">{item.description}</p>
                <button className="card-button">View Details</button>
            </div>
        </div>
    );
};

export default Card;