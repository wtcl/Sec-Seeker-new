import math
import logging
from flask import Flask, request, render_template, session, \
    make_response, url_for, redirect, abort
from flask_admin.actions import action
from flask_admin.contrib import sqla
from flask_admin.menu import MenuLink
from flask_babelex import Babel
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib import sqla
from gps2bd2site import gpstolocation
from SHE import *
import os
import json
import config
import requests
from flask_admin import Admin
from flask_admin.form import SecureForm
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash, check_password_hash
from faker import Faker, Factory
import random
import mypyecharts
from point_in_rectangle import raw_test_in


k0 = 1024
k1 = 40
k2 = 100
n = 9546781931902272913828923724295801735314808738336117082299855267526370781255410204449406183189400394191553500504449780688226003981177767136688893176578431780322420126401247136429165105301768530585293216949048184660695178056521666063185594615709133221269883743509535638513583807607257049234822319285931079665127506948312293265462750992730487096731909922004955846964412738284005178524252365786602967132981374441626648735927147993313988069522138931741286006285375781327263105630906425730759283730995117116175980110578844530483675184106347643567976063814425010197997214633010035560584865048895967251500913096080836509883
length = 1124127490067959807263446365663
p = 103208146936017409001064853981771185455864998286468294292021651567093072755391006690797243062245227974110161616783290449963036069502455840116375500599809354378065508136232575810480600455008819848432899485314223940884758720245320373749115428478542050852778707911799037417936981398197252130697237545750626590533
q = 92500274593832986367397251378162856898838275239456223267003750596901351153941833991986120538983877035861510032124601559966888180086822596869763089693497173235432383986470751400008096226782421678729605536602796869447709469839623881733446440439628853239420308159705321567723006363118922973092807357378500861951

tree = []
tree_len = 5
x1, y1, x2, y2 = 11966845, 4096139, 12078164, 4028802
faketree = [469, 697, 905, 817, 206, 659, 798, 942, 187, 622, 337, 799, 100, 465, 455, 956, 86, 765, 1023, 431, 19, 827, 301, 536, 70, 158, 374, 756, 976, 554, 470, 588, 270, 388, 941, 73, 165, 488, 232, 627, 518, 480, 45, 844, 389, 763, 240, 287, 108, 603, 833, 660, 583, 929, 863, 803, 142, 555, 720, 62, 176, 544, 837, 485, 418, 729, 998, 993, 51, 472, 873, 384, 239, 5, 475, 861, 843, 474, 259, 825, 918, 201, 415, 563, 944, 607, 264, 500, 227, 520, 186, 39, 574, 328, 8, 434, 791, 832, 537, 797, 527, 774, 244, 370, 40, 107, 752, 693, 909, 894, 394, 410, 263, 306, 396, 858, 1003, 18, 188, 675, 860, 135, 426, 883, 816, 255, 210, 505, 571, 277, 699, 320, 71, 911, 74, 486, 351, 535, 140, 327, 404, 824, 354, 892, 674, 153, 549, 940, 340, 288, 27, 766, 907, 722, 522, 900, 295, 189, 151, 175, 539, 377, 854, 362, 332, 886, 511, 162, 967, 110, 739, 468, 792, 23, 1008, 67, 128, 95, 303, 487, 969, 438, 995, 261, 471, 262, 99, 621, 34, 247, 92, 692, 573, 492, 375, 582, 196, 568, 672, 61, 182, 545, 954, 594, 961, 606, 805, 1010, 702, 829, 243, 59, 510, 341, 400, 965, 533, 414, 246, 11, 913, 743, 365, 193, 602, 393, 234, 543, 771, 448, 79, 416, 109, 651, 800, 831, 617, 213, 452, 112, 777, 87, 429, 121, 183, 379, 348, 856, 297, 710, 369, 367, 955, 601, 634, 595, 530, 345, 169, 662, 253, 684, 671, 828, 314, 229, 191, 453, 948, 950, 738, 3, 132, 289, 717, 317, 381, 106, 63, 447, 709, 55, 593, 339, 733, 558, 696, 872, 137, 506, 711, 203, 498, 600, 780, 359, 397, 184, 770, 517, 553, 131, 524, 888, 260, 566, 749, 548, 97, 148, 811, 938, 174, 508, 391, 221, 790, 57, 939, 705, 788, 507, 647, 299, 479, 64, 849, 737, 467, 926, 272, 585, 430, 960, 219, 570, 880, 155, 813, 930, 760, 312, 815, 433, 725, 687, 482, 747, 124, 640, 43, 177, 564, 123, 230, 127, 807, 784, 613, 915, 937, 897, 238, 119, 1004, 546, 41, 616, 719, 390, 54, 267, 789, 946, 512, 992, 273, 1015, 979, 209, 559, 504, 130, 576, 501, 624, 515, 439, 154, 891, 681, 502, 283, 688, 669, 98, 222, 964, 28, 623, 266, 313, 552, 605, 308, 778, 618, 925, 1019, 226, 550, 936, 989, 378, 959, 256, 2, 963, 994, 252, 641, 56, 477, 44, 363, 178, 366, 376, 53, 361, 17, 757, 368, 205, 237, 584, 349, 364, 962, 122, 604, 293, 407, 432, 884, 494, 781, 1020, 493, 149, 190, 516, 35, 572, 409, 65, 235, 231, 982, 286, 88, 890, 104, 526, 324, 701, 291, 307, 528, 881, 629, 208, 685, 896, 521, 882, 565, 931, 425, 741, 276, 577, 609, 315, 347, 138, 392, 645, 458, 612, 852, 980, 562, 597, 945, 152, 451, 436, 801, 424, 1022, 1006, 249, 372, 1021, 678, 168, 1017, 735, 497, 463, 665, 489, 49, 636, 265, 1002, 668, 50, 503, 42, 204, 401, 398, 216, 386, 802, 637, 714, 251, 614, 330, 323, 281, 343, 167, 838, 847, 449, 473, 779, 814, 412, 300, 842, 316, 444, 768, 919, 846, 898, 639, 984, 869, 245, 850, 285, 899, 236, 338, 423, 567, 751, 557, 68, 783, 157, 935, 865, 22, 957, 677, 150, 615, 1, 309, 269, 223, 851, 114, 101, 586, 395, 80, 912, 835, 81, 352, 280, 655, 732, 727, 282, 195, 1001, 643, 133, 745, 927, 274, 953, 764, 459, 921, 290, 906, 31, 908, 356, 541, 619, 16, 48, 445, 598, 373, 862, 26, 514, 592, 319, 910, 523, 77, 818, 331, 812, 648, 83, 867, 476, 405, 143, 20, 194, 278, 580, 333, 848, 578, 37, 302, 509, 311, 385, 810, 579, 730, 632, 417, 839, 670, 656, 170, 454, 60, 611, 866, 357, 819, 758, 625, 334, 809, 496, 821, 654, 754, 804, 199, 120, 718, 160, 304, 76, 630, 1024, 657, 551, 587, 91, 795, 271, 695, 268, 978, 734, 241, 973, 491, 853, 346, 440, 435, 532, 513, 7, 441, 761, 403, 728, 495, 25, 38, 904, 667, 1000, 968, 708, 82, 834, 296, 599, 258, 85, 310, 864, 715, 991, 985, 420, 879, 1005, 707, 242, 93, 589, 680, 1007, 181, 159, 129, 380, 30, 644, 649, 569, 248, 664, 988, 903, 855, 466, 575, 762, 192, 958, 786, 987, 785, 14, 683, 214, 700, 895, 355, 974, 298, 179, 525, 782, 419, 689, 556, 724, 4, 163, 254, 990, 225, 47, 529, 542, 29, 10, 951, 103, 443, 126, 679, 830, 145, 822, 996, 113, 228, 111, 344, 750, 917, 115, 294, 1014, 744, 437, 875, 172, 841, 336, 36, 117, 966, 211, 943, 859, 24, 360, 975, 706, 628, 682, 156, 326, 89, 94, 924, 874, 631, 977, 46, 171, 691, 776, 350, 12, 1016, 499, 118, 638, 902, 292, 652, 534, 690, 836, 200, 450, 726, 383, 704, 650, 321, 371, 934, 1013, 6, 999, 446, 769, 986, 642, 75, 146, 406, 793, 775, 318, 772, 663, 949, 257, 676, 72, 116, 212, 399, 9, 971, 180, 773, 877, 102, 723, 547, 250, 166, 673, 820, 887, 202, 413, 483, 217, 731, 279, 33, 460, 90, 519, 755, 408, 590, 561, 224, 703, 845, 387, 284, 653, 428, 713, 538, 531, 620, 207, 658, 325, 421, 742, 635, 66, 484, 753, 871, 220, 136, 748, 58, 490, 411, 78, 464, 1009, 633, 342, 134, 746, 456, 173, 868, 305, 233, 806, 808, 402, 889, 823, 164, 626, 933, 736, 335, 105, 686, 740, 358, 666, 144, 952, 885, 422, 52, 560, 716, 197, 462, 901, 96, 610, 914, 21, 878, 275, 794, 139, 646, 141, 767, 932, 125, 1018, 329, 382, 461, 840, 983, 928, 581, 661, 198, 32, 796, 1012, 694, 591, 478, 69, 870, 876, 923, 947, 893, 997, 981, 608, 759, 712, 922, 970, 698, 161, 15, 916, 427, 972, 13, 787, 721, 215, 1011, 826, 147, 442, 920, 185, 481, 84, 322, 218, 457, 540, 353, 857, 596]

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __str__(self):
        return self.name


class UserInfo(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.INT(), unique=True, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), unique=False)
    uuid = db.Column(db.String(100), unique=True)
    status = db.Column(db.String(20), unique=False)
    phonenumber = db.Column(db.String(100), unique=False)

    def __repr__(self):
        return self.name+' '+self.password


class CarAdmin(ModelView):
    form_base_class = SecureForm
    column_display_pk = True
    column_searchable_list = ['name', 'status', 'uuid']
    column_filters = ['name', 'status']
    can_view_details = True
    can_export = True
    export_types = ['csv']
    can_set_page_size = True
    column_formatters = dict(
        password=lambda v, c, m, p: '**' + m.password[-6:],
    )


class RoleAdmin(ModelView):
    form_base_class = SecureForm
    column_display_pk = True
    column_searchable_list = ['name', 'id']
    column_filters = ['name']
    can_view_details = True
    can_export = True
    export_types = ['csv']
    can_set_page_size = True


class SliceView(ModelView):
    # 指定模板
    list_template = 'newadmin/list.html'
    create_template = 'newadmin/create.html'
    edit_template = 'newadmin/edit.html'
    details_template = 'newadmin/details.html'

    column_display_pk = True
    column_labels = {
        'id': 'ID',
        'name': 'Name'
    }
    column_searchable_list = ['name', 'status', 'uuid']
    column_filters = ['name', 'status']
    can_view_details = True
    can_export = True
    page_size = True
    export_types = ['csv', 'xlsx']
    can_set_page_size = True


admin = Admin(app, name='疫情防控管理后台', template_mode='bootstrap3')
admin.add_view(CarAdmin(UserInfo, db.session))
# admin.add_view(RoleAdmin(Role, db.session))
# admin = Admin(app=app, name='admin', template_mode='bootstrap3', base_template='newadmin/mylayout.html')  # 指定模板
# admin.add_view(SliceView(UserInfo, db.session, name='数源管理', menu_icon_type='fa', menu_icon_value='fa-table'))
# babel = Babel(app)


def judge(x1, y1, x2, y2, xx, yy):
    # x1,y1表示整个地图的左上上边界，x2，y2代表左下边界，xx,yy是待定位的点
    x_core = x1 / 2 + x2 / 2
    y_core = y1 / 2 + y2 / 2
    global tree
    global tree_len
    if judge_part(x1, y1, x_core, y_core, xx, yy):
        tree.append(1)
        if len(tree) < tree_len:
            judge(x1, y1, x_core, y_core, xx, yy)
    if judge_part(x_core, y_core, x2, y2, xx, yy):
        tree.append(4)
        if len(tree) < tree_len:
            judge(x_core, y_core, x2, y2, xx, yy)
    if judge_part(x1, y_core, x_core, y2, xx, yy):
        tree.append(3)
        if len(tree) < tree_len:
            judge(x1, y_core, x_core, y2, xx, yy)
    if judge_part(x_core, y1, x2, y_core, xx, yy):
        tree.append(2)
        if len(tree) < tree_len:
            judge(x_core, y1, x2, y_core, xx, yy)
    if len(tree) == tree_len:
        return tree


def judge_part(upx, upy, downx, downy, x, y):
    if (upx - x) * (downx - x) <= 0 and (upy - y) * (downy - y) <= 0:
        return True
    else:
        return False


@app.route("/logintest", methods=["GET"])
def logintest():
    if 'name' in session:
        return "Y"
    else:
        return "N"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        print(request.data)
        print(json.loads(request.data))
        name = json.loads(request.data)["name"]
        password = json.loads(request.data)["password"]
        print(name, password)
        result = UserInfo.query.filter_by(name=name).all()
        if len(result) == 1 and check_password_hash(result[0].password,
                                                    password):
            key = str(os.urandom(24))
            session.get(key, '默认值')
            session['name'] = name
            session['password'] = password
            return "1"
        else:
            return "0"
    else:
        return render_template('login.html')


@app.route("/register", methods=["POST"])
def register():
    name = json.loads(request.data)['name']  # 接受登录的用户名
    psd = json.loads(request.data)['password']  # 接受登录的用户密码
    try:
        try:
            info = UserInfo(name=name,
                            password=generate_password_hash(psd),
                            uuid=hex(randint(2**63+1, 2**64-1))[2:],
                            status='nagtive',
                            phonenumber=str(randint(10**11, 10**12-1)))
            db.session.add(info)
            db.session.commit()
            return info.uuid
        except:
            return "No"
    except:
        return "No"


@app.route("/api", methods=["POST"])
def decrypt_data():
    data = json.loads(request.data)["data"]
    # print(data)
    try:
        dd = [decrypt(p, length, d[0]) - decrypt(p, length, d[1]) for d in
              data]
        if max(dd) <= 0:
            return {"res": 1}
        else:
            return {"res": 0}
    except:
        return {"res": 0}


@app.route("/placeapi", methods=["POST"])
def decrypt_data1():
    data = json.loads(request.data)["data"]
    # print(data)
    try:
        dd = [decrypt(p, length, d[0]) - decrypt(p, length, d[1]) for d in
              data]
        if max(dd) <= 0 or min(dd) >= 0:
            return {"res": 1}
        else:
            return {"res": 0}
    except:
        return {"res": 0}


@app.route("/pubkey")
def pubkey():
    r1 = encrypt(p, length, k0, k2, n, 0)
    r2 = encrypt(p, length, k0, k2, n, 0)
    print("pubkey1 : {}\npubkey2 : {}".format(hex(r1)[2:], hex(r2)[2:]))
    return hex(r1)[2:] + "," + hex(r2)[2:]


@app.route("/status", methods=["POST"])
def get_status():
    name = json.loads(request.data)["name"]
    result = UserInfo.query.filter_by(name=name).all()
    if result[0].status == "positive":
        return "1"
    else:
        return "0"


@app.route("/tree", methods=["POST"])
def tree_decrypt():
    tid = json.loads(request.data)["treeid"]
    tid = decrypt(p, length, int(tid, 16))
    if tid in [i for i in range(1024)]:
        tcid = faketree[tid]
        return hex(tcid)[2:]
    else:
        return "hack"


@app.route("/idsearch", methods=["POST"])
def search_id():
    print(request.form["uuids"])
    uuid = request.form["uuids"]
    result = requests.post("http://127.0.0.1:8081/idsearch",
                           json.dumps({"role": "admin", "uuid": uuid}))
    result = result.text.split("<br>")
    print(result)
    fake1 = Factory.create()
    one_data = {}
    one_data1 = {}
    for i in range(len(result)):
        one_data[i + 1] = [fake1.name(), str(random.randint(10**11, 10**12-1)),
                       random.choice(["nagtive", "positive"])]
        one_data1[i + 1] = ["", "", ""]
    return render_template('admin/x.html', data_dict1=one_data,
                           data_dict2=one_data1)


@app.route("/placesearch", methods=["POST"])
def search_place():
    global tree
    global tree_len
    print(request.form["times"])
    print(request.form["points"])
    tse = request.form["times"].split(",")
    points = request.form["points"].split(";")
    area = [xy.split(",") for xy in points]
    area = [[int(xy[0]), int(xy[1])] for xy in area]
    # tree_len = 5
    x1, y1, x2, y2 = 11966845, 4096139, 12078164, 4028802
    # area = [[12000000, 4030000], [12060000, 4030000],
    #         [12060000, 4060000], [12000000, 4030000],
    #         [12000000, 4030000]]
    treeid = []
    treex = [x1 + 111319 / 64 + (111319 / 32) * i for i in range(32)]
    treey = [y2 + 67337 / 64 + (67337 / 32) * i for i in range(32)]
    for x in treex:
        for y in treey:
            if raw_test_in(area, [x, y]):
                r = judge(x1, y1, x2, y2, x, y)
                tree = []
                treeid.append(faketree[(r[0] - 1) * 256 + (r[1] - 1) * 64 + (
                            r[2] - 1) * 16 + (r[3] - 1) * 4 + (r[4] - 1)])
    # 只是加入了各个节点
    for a in area:
        r = judge(x1, y1, x2, y2, a[0], a[1])
        tree = []
        treeid.append(faketree[(r[0] - 1) * 256 + (r[1] - 1) * 64 + (
                    r[2] - 1) * 16 + (r[3] - 1) * 4 + (r[4] - 1)])
    for i in range(len(area)):
        area[i][0] = encrypt(p, length, k0, k2, n, -area[i][0])
        area[i][1] = encrypt(p, length, k0, k2, n, -area[i][1])
    print(treeid)
    result = requests.post("http://127.0.0.1:8081/placesearch",
                           data=json.dumps({"starttime": tse[0],
                                            "endtime": tse[1],
                                            "treeid": treeid,
                                            "area": area}))
    result = result.text.split("<br>")
    print(result)
    fake2 = Factory.create()
    two_data = {}
    two_data1 = {}
    for i in range(len(result)):
        two_data[i + 1] = [fake2.name(),
                           str(random.randint(10 ** 11, 10 ** 12 - 1)),
                           random.choice(["nagtive", "positive"])]
        two_data1[i + 1] = ["", "", ""]
    return render_template('admin/x.html', data_dict1=two_data1,
                           data_dict2=two_data)


@app.route("/relasearch", methods=["POST", "GET"])
def relasearch():
    print(request.form["uuids"])
    uuid = request.form["uuids"]
    result = requests.post("http://127.0.0.1:8081/relasearch",
                           json.dumps({"uuids": uuid}))
    result = json.loads(result.text)["res"]
    print(result)
    g = mypyecharts.RelationshipGraph()
    r = []
    for i in range(len(result)):
        r.append(((result[i][0], ""), (result[i][1], "")))
    g.add_list(r)
    g.render()
    g.save("./static/pycahrt/base.html")
    return render_template('admin/x.html', data_dict1={}, data_dict2={})


@app.route("/show", methods=["GET", "POST"])
def show_result():
    data = {
        1: ['jiaqi', '15216262345', '阴性'],
        2: ['yandi', '11896149631', '阴性'],
        3: ['jiebro', '16652496946', '阴性'],
        4: ['haohao', '15216234346', '阴性'],
        5: ['xinyi', '11896134961', '阴性'],
        6: ['jiaojiao', '16524969446', '阴性']
    }
    return render_template('admin/x.html', data_dict1=data,
                           data_dict2=data)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)
