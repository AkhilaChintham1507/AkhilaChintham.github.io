from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder='./templates',static_folder="./static")

accounts = {
    '123456': {'name': 'John Doe', 'balance': 1000}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    if request.method == 'POST':
        account_number = request.form['account_number']
        amount = float(request.form['amount'])
        transaction_type = request.form['transaction_type']

        if account_number in accounts:
            if transaction_type == 'deposit':
                accounts[account_number]['balance'] += amount
            elif transaction_type == 'withdrawal':
                if amount <= accounts[account_number]['balance']:
                    accounts[account_number]['balance'] -= amount
                else:
                    return "Insufficient funds for withdrawal."
            else:
                return "Invalid transaction type."
        else:
            return "Account not found."

    return render_template('transactions.html', accounts=accounts)

if __name__ == '__main__':
    app.run(debug=True)
