CODE 3 Validating the ui of react app with object-json

import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Form from './Form';

describe('Form Component', () => {
  const formFields = {
    name: 'John Doe',
    email: 'john@example.com',
    message: 'Hello, world!',
    mobile: '1234567890'
  };

  test('renders form fields', () => {
    render(<Form />);
    
    const nameInput = screen.getByLabelText('Name');
    const emailInput = screen.getByLabelText('Email');
    const messageInput = screen.getByLabelText('Message');
    const mobileInput = screen.getByLabelText('Mobile');
    
    expect(nameInput).toBeInTheDocument();
    expect(emailInput).toBeInTheDocument();
    expect(messageInput).toBeInTheDocument();
    expect(mobileInput).toBeInTheDocument();
  });

  test('validates form submission', () => {
    render(<Form />);
    
    const nameInput = screen.getByLabelText('Name');
    const emailInput = screen.getByLabelText('Email');
    const messageInput = screen.getByLabelText('Message');
    const mobileInput = screen.getByLabelText('Mobile');
    const submitButton = screen.getByRole('button', { name: 'Submit' });
    
    // Submit form without filling any fields
    fireEvent.click(submitButton);
    expect(screen.getByText('Name is required')).toBeInTheDocument();
    expect(screen.getByText('Email is required')).toBeInTheDocument();
    expect(screen.getByText('Message is required')).toBeInTheDocument();
    expect(screen.getByText('Mobile is required')).toBeInTheDocument();
    
    // Fill in the form fields
    userEvent.type(nameInput, formFields.name);
    userEvent.type(emailInput, formFields.email);
    userEvent.type(messageInput, formFields.message);
    userEvent.type(mobileInput, formFields.mobile);
    
    // Submit the form
    fireEvent.click(submitButton);
    
    // Verify that the success message is displayed
    expect(screen.getByText('Form submitted successfully')).toBeInTheDocument();
  });

  test('validates email format', () => {
    render(<Form />);
    
    const emailInput = screen.getByLabelText('Email');
    const submitButton = screen.getByRole('button', { name: 'Submit' });
    
    // Fill in the email field with an invalid email format
    userEvent.type(emailInput, 'invalid-email');
    
    // Submit the form
    fireEvent.click(submitButton);
    
    // Verify that the email validation error message is displayed
    expect(screen.getByText('Invalid email format')).toBeInTheDocument();
    
    // Clear the email field
    userEvent.clear(emailInput);
    
    // Fill in the email field with a valid email format
    userEvent.type(emailInput, 'valid-email@example.com');
    
    // Submit the form
    fireEvent.click(submitButton);
    
    // Verify that the success message is displayed
    expect(screen.getByText('Form submitted successfully')).toBeInTheDocument();
  });

  test('validates mobile number format', () => {
    render(<Form />);
    
    const mobileInput = screen.getByLabelText('Mobile');
    const submitButton = screen.getByRole('button', { name: 'Submit' });
    
    // Fill in the mobile number field with an invalid format
    userEvent.type(mobileInput, 'invalid-number');
    
    // Submit the form
    fireEvent.click(submitButton);
    
    // Verify that the mobile number validation error message is displayed
    expect(screen.getByText('Invalid mobile number format')).toBeInTheDocument();
    
    // Clear the mobile number field
    userEvent.clear(mobileInput);
    
    // Fill in the mobile number field with a valid format
    userEvent.type(mobileInput, '1234567890');
    
    // Submit the form
    fireEvent.click(submitButton);
    
    // Verify that the success message is displayed
    expect(screen.getByText('Form submitted successfully')).toBeInTheDocument();
  });
});
