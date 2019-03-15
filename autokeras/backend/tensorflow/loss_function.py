import tensorflow as tf


def classification_loss(prediction, label):
    return tf.keras.losses.categorical_crossentropy(y_pred=tf.nn.softmax(prediction, axis=-1), y_true=label, axis=-1)  # ,from_logits=True
    # return -tf.reduce_sum(tf.nn.log_softmax(prediction) * label, 1)


def regression_loss(prediction, target):
    return tf.keras.losses.mean_squared_error(y_pred=prediction, y_true=target)


def binary_classification_loss(prediction, label):
    return tf.keras.losses.binary_crossentropy(y_pred=tf.nn.sigmoid(prediction), y_true=label, axis=-1)  # ,from_logits=True
