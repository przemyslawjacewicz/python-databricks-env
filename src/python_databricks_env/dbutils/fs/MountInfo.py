class MountInfo:
    def __init__(self, mountPoint: str, source: str, encryptionType: str):
        self.mountPoint = mountPoint
        self.source = source
        self.encryptionType = encryptionType

    def __str__(self):
        return f"MountInfo(mountPoint={self.mountPoint}, source={self.source}, encryptionType={self.encryptionType})"
