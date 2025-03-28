import React, { useState } from 'react';
import './StringCalculator.css';

/**
 * StringCalculator Component
 *
 * A simple React component that allows users to input a string of numbers,
 * sends it to the backend for calculation, and displays the result or error messages.
 */

const StringCalculator = () => {
    const [input, setInput] = useState('');
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    /**
     * Sends the input string to the backend API for calculation.
     * Updates the state with the result or an error message.
     */
    const handleCalculate = async () => {
        setResult(null);
        setError(null);
        setIsLoading(true);

        try {
            const response = await fetch('http://localhost:5000/calculate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ numbers: input.replace(/\\n/g, '\n') }),
            });

            const data = await response.json();

            if (response.ok) {
                setResult(data.result);
            } else {
                setError(data.error || 'An unexpected error occurred');
            }
        } catch (error) {
            console.error('Calculation error:', error);
            setError(error.message || 'Network error or server unavailable');
        } finally {
            setIsLoading(false);
        }
    };

    /**
     * Handles the Enter key press to trigger calculation.
     * @param {Event} e - The keyboard event object.
     */

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            handleCalculate();
        }
    };

    return (
        <div className="calculator-container">
            <div className="calculator-box">
                <h1>String Calculator</h1>
                <input
                    type="text"
                    placeholder="Enter numbers"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={handleKeyPress}
                    className="calculator-input"
                />
                <button 
                    onClick={handleCalculate} 
                    className="calculator-button"
                    disabled={isLoading}
                >
                    {isLoading ? 'Calculating...' : 'Calculate'}
                </button>
                {result !== null && <p className="calculator-result">Result: {result}</p>}
                {error && <p className="calculator-error">Error: {error}</p>}
            </div>
        </div>
    );
};

export default StringCalculator;
