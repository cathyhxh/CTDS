REGISTRY = {}

from .basic_controller import BasicMAC
REGISTRY["basic_mac"] = BasicMAC

from .tea_controller import TeaMAC
REGISTRY["teacher_mac"] = TeaMAC

from .stu_controller import StuMAC
REGISTRY["student_mac"] = StuMAC
