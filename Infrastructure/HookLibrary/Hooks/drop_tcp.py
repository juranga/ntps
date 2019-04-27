def drop_tcp(packet)
    idx = 1
    while True:
        layer = packet.getlayer(idx)
        if layer is None:
            break
        if layer.name == "TCP":
            return None
        yield layer
        idx += 1

    return packet, "Drop"