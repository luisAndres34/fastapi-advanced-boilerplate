import time


def send_notification_email(email: str, message: str) -> None:
    print(f"Enviando correo a {email}: {message}")
    time.sleep(3)
    print(f"El correo fue exitosamente enviado a {email}!")


def write_audit_log(item_id: int, new_price: int) -> None:
    with open("./log_precios.txt", "a") as logs:
        logs.write(f"El producto {item_id} cambió su precio a ${new_price}\n")

def export_csv():
    time.sleep(5)
    with open("./export.csv", "w") as export:
        export.write("Exported")

    print("Exportación completada.")
    