from flask import Blueprint, jsonify, request, redirect
import stripe
import yaml

bp = Blueprint('chatbot', __name__)

# Load configuration from YAML
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)
    # Set the Stripe secret key from YAML config
    stripe.api_key = config['stripe']['secret_key']


# Route for the chatbot
@bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').lower()
    if user_message == "hello":
        response = "Hi there!"
    elif user_message == "bye":
        response = "Goodbye!"
    else:
        response = "Hello! How can I assist you today?"
    return jsonify({"response": response})


@bp.route('/pay', methods=['POST'])
def create_checkout_session():
    try:
        # Create Stripe checkout session with test product data from YAML
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': config['stripe']['currency'],
                    'product_data': {
                        'name': 'Chatbot Service',
                    },
                    'unit_amount': config['stripe']['product_price'],  # Product price in cents from YAML
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:5000/success',
            cancel_url='http://127.0.0.1:5000/cancel',
        )
        return jsonify({
            'checkout_url': session.url
        })
    except Exception as e:
        return jsonify(error=str(e)), 500
