def change_tcp(packet)
    idx = 1
    while True:
        layer = packet.getlayer(idx)
        if layer is None:
            break
        del layer.chksum
        if layer.name == "TCP":
            layer["TCP"].src = 55555
            break
        yield layer
        idx += 1

    return packet.__class__(str(packet)), "modification"

        
