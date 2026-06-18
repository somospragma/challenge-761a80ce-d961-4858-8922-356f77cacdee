from src.models.transaction_model import Transaction
from src.config.aws_config import sqs_client

@tracer.capture_method
def handle_transaction(data):
    logger.info('Handling transaction')
    transaction = Transaction(**data)
    send_to_sqs(transaction)
    return transaction

def send_to_sqs(transaction):
    response = sqs_client.send_message(
        QueueUrl=os.getenv('SQS_QUEUE_URL'),
        MessageBody=transaction.json()
    )
    logger.info(f'Message sent to SQS: {response}')