#MASIH BELUM FIX, AKU TAMBAHIN BESOK GUYS


from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# Simulasi database
transactions = []

# Endpoint untuk membuat transaksi
@app.route('/api/pay', methods=['POST'])
def create_payment():
    try:
        # Ambil data dari request
        data = request.json
        user_id = data['user_id']
        service_id = data['service_id']
        amount = data['amount']

        # Buat transaksi baru
        transaction_id = str(uuid.uuid4())
        transaction = {
            "transaction_id": transaction_id,
            "user_id": user_id,
            "service_id": service_id,
            "amount": amount,
            "status": "pending",  # Status awal transaksi
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        transactions.append(transaction)

        # Informasikan pengguna untuk melakukan transfer
        bank_details = {
            "bank_name": "Bank ABC",
            "account_number": "1234567890",
            "account_name": "Your Company Name",
            "amount": amount,
            "reference_code": transaction_id
        }

        return jsonify({
            "message": "Please transfer the amount to the following bank account",
            "bank_details": bank_details,
            "transaction": transaction
        }), 201

    except Exception as e:
        return jsonify({
            "message": "Failed to create payment",
            "error": str(e)
        }), 500


# Endpoint untuk memvalidasi pembayaran (manual)
@app.route('/api/pay/validate', methods=['POST'])
def validate_payment():
    try:
        # Ambil data
