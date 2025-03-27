import { useState } from 'react';

const StringCalculator = () => {
    const [input, setInput] = useState('');
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);

    const handleCalculate = async () => {
        console.log('Sending request to backend...', input);
        try {
            const response = await fetch('http://localhost:5000/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ numbers: input }),
            });

            const data = await response.json();

            if (response.ok) {
                setResult(data.result);
                setError(null);
            } else {
                setError(data.error || 'An error occurred');
                setResult(null);
            }
        } catch (error) {
            console.error('Fetch error:', error);
            setError('Network error or server unavailable');
            setResult(null);
        }
    };

    return (
        <div>
            <h1>String Calculator</h1>
            <input
                type="text"
                placeholder="Enter numbers"
                value={input}
                onChange={(e) => setInput(e.target.value)}
            />
            <button onClick={handleCalculate}>Calculate</button>
            {result !== null && <p>Result: {result}</p>}
            {error && <p style={{color: 'red'}}>Error: {error}</p>}
        </div>
    );
};

export default StringCalculator;