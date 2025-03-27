import { render, screen } from '@testing-library/react';
import StringCalculator from '../components/StringCalculator';

test('renders StringCalculator component', () => {
  render(<StringCalculator />);
  const headingElement = screen.getByText(/String Calculator/i);
  expect(headingElement).toBeInTheDocument();
});
