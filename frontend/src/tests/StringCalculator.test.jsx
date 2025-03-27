import { fireEvent, render, screen } from '@testing-library/react';
import StringCalculator from '../components/StringCalculator';

test('renders StringCalculator component', () => {
  render(<StringCalculator />);
  const headingElement = screen.getByText(/String Calculator/i);
  expect(headingElement).toBeInTheDocument();
});

test('renders input field and button', () => {
    render(<StringCalculator />);
    const inputElement = screen.getByPlaceholderText(/Enter numbers/i);
    const buttonElement = screen.getByText('Calculate');

    expect(inputElement).toBeInTheDocument();
    expect(buttonElement).toBeInTheDocument();
  });

test('displays result after calculation', async () => {
    render(<StringCalculator />);
    const inputElement = screen.getByPlaceholderText(/Enter numbers/i);
    const buttonElement = screen.getByText('Calculate');

    fireEvent.change(inputElement, { target: { value: '1,2,3' } });
    fireEvent.click(buttonElement);

    const resultElement = await screen.findByText(/Result:/i);
    expect(resultElement).toBeInTheDocument();
  });