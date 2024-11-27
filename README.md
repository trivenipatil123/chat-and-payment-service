
# Chatbot API with Stripe Payment Integration

This is a simple Flask-based API that simulates basic chatbot interactions and includes a Stripe payment flow. The API includes two routes: 
- `/chat`: Accepts a user message and responds with predefined chatbot replies.
- `/pay`: Integrates Stripe to simulate a checkout session for a $5 "Chatbot Service".

## Requirements

- Python 3.7+
- Stripe account (for API keys, using test mode)

## Features

1. **Chatbot Interaction**: Responds to specific user messages like "hello" and "bye", or provides a default response.
2. **Stripe Payment**: Simulates a payment flow using Stripe’s test environment, allowing a user to pay for "Chatbot Service" costing $5.

## Setup and Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/your-repo/chatbot-stripe-api.git
cd chatbot-stripe-api
```

### Step 2: Create a virtual environment (optional, but recommended)
```bash
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate    # For Windows
```

### Step 3: Install dependencies
Ensure you have `pip` installed, then run:
```bash
pip install -r requirements.txt
```

This will install the following packages:
- Flask (web framework)
- Stripe (for payment integration)

### Step 4: Set up Stripe keys
You'll need Stripe API keys for this project. You can get them from the Stripe dashboard in test mode.

#### Option 1: Set API keys in environment variables (recommended)
Set your Stripe secret key in an environment variable:
```bash
export STRIPE_SECRET_KEY='your_stripe_secret_key'  # For macOS/Linux
set STRIPE_SECRET_KEY='your_stripe_secret_key'     # For Windows
```

#### Option 2: Hardcode keys (for testing)
You can also modify the code in `routes.py` to include your Stripe secret key directly:
```python
stripe.api_key = "your_stripe_secret_key"
```

### Step 5: Run the application
Run the app using the following command:
```bash
python run.py
```

This will start the Flask application in development mode at `http://127.0.0.1:5000`.

## API Endpoints

### 1. `/chat` (POST)
This route simulates a chatbot interaction. It accepts a JSON payload with a `message` field, and the chatbot responds based on the message content.

#### Request Example:
```bash
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "hello"}'
```

#### Response Example:
```json
{
  "response": "Hi there!"
}
```

- If the user sends `"hello"`, the response will be `"Hi there!"`
- If the user sends `"bye"`, the response will be `"Goodbye!"`
- For any other message, the response will be `"Hello! How can I assist you today?"`

### 2. `/pay` (POST)
This route creates a Stripe checkout session for a service costing $5. It returns a Stripe Checkout URL that can be used to complete the payment.

#### Request Example:
```bash
curl -X POST http://127.0.0.1:5000/pay
```

#### Response Example:
```json
{
  "checkout_url": "https://checkout.stripe.com/pay/cs_test_xxxxxxxxxxxxxxxxxxxxx"
}
```

You can use the returned `checkout_url` to open the Stripe checkout page in your browser and complete the test payment.

### Testing the Stripe Payment Flow
- Stripe test cards can be used to simulate payments. For example, use the card number `4242 4242 4242 4242` with any valid expiration date and CVC.
- You will be redirected to a success or cancel page based on whether the payment was successful or not.

## Running Tests

You can use tools like `Postman` or `curl` to send test requests to the API and validate that both routes work as expected.

## Stripe Test Mode
This project uses Stripe’s test mode, so no real transactions will be processed. You can monitor all test transactions in your [Stripe dashboard](https://dashboard.stripe.com/test/dashboard).

## Additional Information

### Key Files:
- `app/__init__.py`: Initializes the Flask app.
- `app/routes.py`: Contains the chatbot and payment routes.
- `run.py`: Entry point to start the Flask server.

### Stripe Configuration
The `STRIPE_SECRET_KEY` should be kept confidential. For production use, always load sensitive keys from environment variables rather than hardcoding them in your code.
