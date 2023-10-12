from SHE import *

k0 = 1024
k1 = 40
k2 = 100
n = 9546781931902272913828923724295801735314808738336117082299855267526370781255410204449406183189400394191553500504449780688226003981177767136688893176578431780322420126401247136429165105301768530585293216949048184660695178056521666063185594615709133221269883743509535638513583807607257049234822319285931079665127506948312293265462750992730487096731909922004955846964412738284005178524252365786602967132981374441626648735927147993313988069522138931741286006285375781327263105630906425730759283730995117116175980110578844530483675184106347643567976063814425010197997214633010035560584865048895967251500913096080836509883
length = 1124127490067959807263446365663
p = 103208146936017409001064853981771185455864998286468294292021651567093072755391006690797243062245227974110161616783290449963036069502455840116375500599809354378065508136232575810480600455008819848432899485314223940884758720245320373749115428478542050852778707911799037417936981398197252130697237545750626590533
q = 92500274593832986367397251378162856898838275239456223267003750596901351153941833991986120538983877035861510032124601559966888180086822596869763089693497173235432383986470751400008096226782421678729605536602796869447709469839623881733446440439628853239420308159705321567723006363118922973092807357378500861951


def raw_test_in(area, point):
    # area = [[0, 0], [2, 0], [2, 2], [0, 2], [0, 0]]
    # area = [[11966845, 4028802], [12078164, 4028802],
    #         [12078164, 4096139], [11966845, 4096139],
    #         [11966845, 4028802]]
    # point = [12077531, 4095657]
    verify = []
    for i in range(len(area)-1):
        p0 = area[i]
        p1 = area[i+1]
        x1 = (point[0] - p0[0])
        y1 = (point[1] - p0[1])
        x2 = (point[0] - p1[0])
        y2 = (point[1] - p1[1])
        # print(point[0], p0[0], x1)
        # print(point[1], p0[1], y1)
        # print(point[0], p1[0], x2)
        # print(point[1], p1[1], y2)
        verify.append((x1*y2, x2*y1))
        # verify.append((point[0]*point[1]+p0[0]*p1[1]+point[1]*p1[0]+p0[1]*point[0]),
        #               (point[0]*point[1]+p0[1]*p1[0]+point[0]*p1[1]+p0[0]*point[1]))
    verify = [d[0] - d[1] for d in verify]
    # print(verify)
    if max(verify) <= 0 or min(verify) >= 0:
        # print("in")
        return True
    else:
        # print("no_in")
        return False


def test_in():
    # area = [[0, 0], [2, 0], [2, 2], [0, 2], [0, 0]]
    area = [[11966845, 4028802], [11966845, 4096139],
            [12078164, 4096139], [12078164, 4028802],
            [11966845, 4028802]]
    point = [encrypt(p, length, k0, k2, n, 12077531),
             encrypt(p, length, k0, k2, n, 4095657)]
    area_sub = [[-a[0], -a[1]] for a in area]

    for i in range(len(area)):
        area[i][0] = encrypt(p, length, k0, k2, n, area[i][0])
        area[i][1] = encrypt(p, length, k0, k2, n, area[i][1])
        area_sub[i][0] = encrypt(p, length, k0, k2, n, area_sub[i][0])
        area_sub[i][1] = encrypt(p, length, k0, k2, n, area_sub[i][1])
    print(area_sub)
    print(point)
    verify = []
    for i in range(len(area)-1):
        p0 = area_sub[i]
        p1 = area_sub[i+1]
        # x1 = (point[0] - p0[0])
        # y1 = (point[1] - p0[1])
        # x2 = (point[0] - p1[0])
        # y2 = (point[1] - p1[1])
        x1 = (point[0] + p0[0])
        y1 = (point[1] + p0[1])
        x2 = (point[0] + p1[0])
        y2 = (point[1] + p1[1])
        print(decrypt(p, length, x1))
        print(decrypt(p, length, y1))
        print(decrypt(p, length, x2))
        print(decrypt(p, length, y2))
        verify.append((x1*y2, x2*y1))
    print([decrypt(p, length, d[0]) for d in verify] +
          [decrypt(p, length, d[1]) for d in verify])
    verify = [decrypt(p, length, d[0]) -
              decrypt(p, length, d[1])
              for d in verify]
    print(verify)
    if max(verify) <= 0 or min(verify) >= 0:
        print("in")
    else:
        print("no_in")


if __name__ == "__main__":
    area = [[0, 0], [2, 0], [2, 2], [0, 2], [0, 0], [0, 0]]
    point = [1, 1]
    print(raw_test_in(area, point))
    # test_in()
