def change_dns(packet)
    idx = 1
    while True:
        layer = packet.getlayer(idx)
        if layer is None:
            break
        del layer.chksum
        if layer.name == "DNS":
            layer["DNS"].src = 44444
            break
        yield layer
        idx += 1

    return packet.__class__(str(packet)), "Modification"