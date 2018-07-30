from django.shortcuts import render, render_to_response
from . import models
import datetime
import request
from . import data_json

# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import HttpResponse
# from django.template import RequestContext

wor_infos = data_json.error_json()
tklist = json_list = data_json.get_json()
tklist = json_list = json_list[::-1]


def index(rq):
    '''
    首页展示数据计算和传递
    :param rq:
    :return:
    '''
    # 所有数据
    # tklist = models.Rent12.objects.all()

    # 已有数据数
    counts = len(json_list)
    # 异常数据
    # wor_infos = models.Rent12.objects.raw('select * from rent.rent_12 where (abs(rent_money-pred_money)/rent_money)>1')
    # 异常数量
    wor_num = len(list(wor_infos))
    # 本页展示数量
    show_num = len(list(tklist[:30]))
    # 当前时间
    t_n = datetime.datetime.now().strftime('%H:%M:%S')
    # 异常占比
    wor_pr = round((wor_num / counts) * 100, 2)
    # 未展示
    also_has = counts - show_num
    # 正常
    normal = counts - wor_num
    # 正常占比
    nor_pr = 100 - wor_pr

    # 传递参数
    return render(rq, 'show/index.html',
                  {
                      'tklist': tklist[:30],
                      'counts': counts,
                      'wor_infos': wor_infos,
                      'wor_num': wor_num,
                      'show_num': show_num,
                      't_n': t_n,
                      'wor_pr': wor_pr,
                      'also_has': also_has,
                      'normal': normal,
                      'nor_pr': nor_pr,
                  })


def hole_list(rq):
    '''
    显示全部条目
    :param rq:
    :return:
    '''
    # 所有数据
    # tklist = models.Rent12.objects.all().reverse()

    # 分页操作
    # paginator = Paginator(tklist, 50)
    # page = request.GET.get('page')
    #
    # try:
    #     houses = paginator.page(page)
    # except PageNotAnInteger:
    #     houses = paginator.page(1)
    # except EmptyPage:
    #     houses = paginator.page(paginator.num_pages)

    # 已有数据数
    counts = len(json_list)
    # 异常数据
    # wor_infos = models.Rent12.objects.raw('select * from rent.rent_12 where (abs(rent_money-pred_money)/rent_money)>1')
    # 异常数量
    wor_num = len(list(wor_infos))
    # 本页展示数量
    show_num = len(list(json_list[:30]))
    # 当前时间
    t_n = datetime.datetime.now().strftime('%H:%M:%S')
    # 异常占比
    wor_pr = round((wor_num / counts) * 100, 2)
    # 未展示
    also_has = counts - show_num
    # 正常
    normal = counts - wor_num
    # 正常占比
    nor_pr = 100 - wor_pr

    # posts = tklist

    ONE_PAGE_OF_DATA = 50

    try:
        curPage = int(rq.GET.get('curPage', '1'))
        allPage = int(rq.GET.get('allPage', '1'))
        pageType = str(rq.GET.get('pageType', ''))
    except ValueError:
        curPage = 1
        allPage = 1
        pageType = ''

    # 判断点击了【下一页】还是【上一页】
    if pageType == 'pageDown':
        curPage += 1
    elif pageType == 'pageUp':
        curPage -= 1

    startPos = (curPage - 1) * ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    posts = tklist[startPos:endPos]

    if curPage == 1 and allPage == 1:  # 标记1
        allPostCounts = counts
        allPage = allPostCounts / ONE_PAGE_OF_DATA
        remainPost = allPostCounts % ONE_PAGE_OF_DATA
        if remainPost > 0:
            allPage += 1

    return render(rq,
                  'show/hole_list.html',
                  {
                      'posts': posts,
                      'wor_infos': wor_infos,
                      'wor_num': wor_num,
                      'show_num': show_num,
                      't_n': t_n,
                      'wor_pr': wor_pr,
                      'also_has': also_has,
                      'normal': normal,
                      'nor_pr': nor_pr,
                      'counts': counts,
                      'allPage': allPage,
                      'curPage': curPage,
                  },
                  )


def by_province(rq):
    '''
    由省份查询列表
    :param rq:
    :return:
    '''
    return render(rq, 'show/by_province.html', {})


def by_city(rq):
    '''
    由城市查询列表
    :param rq:
    :return:
    '''
    return render(rq, 'show/by_city.html', {})

    # def detail(rq):
    '''
    显示目标详情
    :param rq:
    :return:
    '''
    # if request.methods == 'GET':
    # city = request.GET['city']
    # house_area = request.GET['house_area']
    # rent_money = request.GET['rent_money']
    # floor = request.GET['floor']
    # pred_money = request.GET['pred_money']

    # print("GET:%s" % house_area)
    # print("GET:%s" % rent_money)
    # print("GET:%s" % city)
    # print("GET:%s" % floor)
    # print("GET:%s" % pred_money)
    #
    # item_info = models.Rent12.objects.get(pred_money=pred_money, house_area=house_area, rent_money=rent_money, city=city, floor=floor)
    #
    #
    # return render(rq, 'show/detail.html', {'item_info':item_info})


# def detail_id(rq, idint):
#     '''
#     显示目标详情
#     :param rq:
#     :return:
#     '''
#     # 目标条目
#     item_info = models.Rent12.objects.select_related().get(id=idint)
#     # item_info = models.Rent12.objects.extra('SELECT * FROM id = %s' % idint)
#     # print(type(item_info))
#     # 同城房源数
#     hnum_city = models.Rent12.objects.select_related().filter(city=item_info.city)
#     hnum_city_num = len(list(hnum_city))
#
#     # 同城异常数
#
#     err_num = 0
#     for info in hnum_city:
#         if info in wor_infos:
#             err_num += 1
#     error_num = err_num
#     # 同城正常数
#     nor_num = hnum_city_num - error_num
#     # 正常占比
#     nor_pr = round((nor_num / hnum_city_num) * 100, 2)
#     # 异常占比
#     err_pr = round((100 - nor_pr), 2)
#     # 当前时间
#     t_n = datetime.datetime.now().strftime('%H:%M:%S')
#     # 还有
#     also_has = hnum_city_num - 1
#
#     region = item_info.region
#     province = item_info.province
#     city = item_info.city
#     room = item_info.room
#     hall = item_info.hall
#     toilet = item_info.toilet
#     house_area = item_info.house_area
#     rent_money = item_info.rent_money
#     level = item_info.level
#     floor = item_info.floor
#     toward = item_info.toward
#     facility = item_info.facility
#     pred_money = item_info.pred_money
#
#     return render(rq,
#                   'show/detail_id.html',
#                   {
#                       'hnum_city_num': hnum_city_num,
#                       'item_info': item_info,
#                       'hnum_city': hnum_city,
#                       'error_num': error_num,
#                       'nor_num': nor_num,
#                       'nor_pr': nor_pr,
#                       'err_pr': err_pr,
#                       't_n': t_n,
#                       'also_has': also_has,
#                       'wor_infos': wor_infos,
#                       'region': region,
#                       'province': province,
#                       'city': city,
#                       'room': room,
#                       'hall': hall,
#                       'toilet': toilet,
#                       'house_area': house_area,
#                       'rent_money': rent_money,
#                       'level': level,
#                       'floor': floor,
#                       'toward': toward,
#                       'facility': facility,
#                       'pred_money': pred_money,
#
#                   }
#                   )


def detail_id(rq, idint):
    '''
    显示目标详情
    :param rq:
    :return:
    '''
    # 目标条目
    for dit in json_list:
        if dit.get('id') == int(idint):
            region = dit.get('region')
            province = dit.get('province')
            city = dit.get('city')
            room = dit.get('room')
            hall = dit.get('hall')
            toilet = dit.get('toilet')
            house_area = dit.get('house_area')
            rent_money = dit.get('rent_money')
            level = dit.get('level')
            floor = dit.get('floor')
            toward = dit.get('toward')
            facility = dit.get('facility')
            pred_money = dit.get('pred_money')
            item_info = dit
            # item
    # item_info = models.Rent12.objects.select_related().get(id=idint)
    # 同城房源数
    hnum_city = []
    for ifo in json_list:
        if ifo.get('city') == city:
            hnum_city.append(ifo)
    # hnum_city = models.Rent12.objects.select_related().filter(city=city)
    hnum_city_num = len(hnum_city)

    # 同城异常数
    err_num = 0
    for info in hnum_city:
        if info in wor_infos:
            err_num += 1
    error_num = err_num
    # 同城正常数
    nor_num = hnum_city_num - error_num
    # 正常占比
    nor_pr = round((nor_num / hnum_city_num) * 100, 2)
    # 异常占比
    err_pr = round((100 - nor_pr), 2)
    # 当前时间
    t_n = datetime.datetime.now().strftime('%H:%M:%S')
    # 还有
    also_has = hnum_city_num - 1

    return render(rq,
                  'show/detail_id.html',
                  {
                      'hnum_city_num': hnum_city_num,
                      'item_info': item_info,
                      'hnum_city': hnum_city,
                      'error_num': error_num,
                      'nor_num': nor_num,
                      'nor_pr': nor_pr,
                      'err_pr': err_pr,
                      't_n': t_n,
                      'also_has': also_has,
                      'wor_infos': wor_infos,
                      'region': region,
                      'province': province,
                      'city': city,
                      'room': room,
                      'hall': hall,
                      'toilet': toilet,
                      'house_area': house_area,
                      'rent_money': rent_money,
                      'level': level,
                      'floor': floor,
                      'toward': toward,
                      'facility': facility,
                      'pred_money': pred_money,

                  }
                  )


def detail_city(rq, city_str):
    '''
    显示目标详情
    :param rq:
    :return:
    '''
    tklist = []
    for info in json_list:
        if info.get('city') == city_str:
            tklist.append(info)
    # 已有数据数
    counts = len(tklist)
    # 异常数据
    # wor_infos = models.Rent12.objects.raw('select * from rent.rent_12 where (abs(rent_money-pred_money)/rent_money)>1')
    # 异常数量
    err_num = 0
    for info in tklist:
        if info in wor_infos:
            err_num += 1
    wor_num = err_num
    # 本页展示数量
    show_num = len(tklist)
    # 当前时间
    t_n = datetime.datetime.now().strftime('%H:%M:%S')
    # 异常占比
    wor_pr = round((wor_num / counts) * 100, 2)
    # 未展示
    also_has = counts - show_num
    # 正常
    normal = counts - wor_num
    # 正常占比
    nor_pr = 100 - wor_pr

    posts = tklist

    return render(rq,
                  'show/hole_list.html',
                  {
                      'posts': posts,
                      'wor_infos': wor_infos,
                      'wor_num': wor_num,
                      'show_num': show_num,
                      't_n': t_n,
                      'wor_pr': wor_pr,
                      'also_has': also_has,
                      'normal': normal,
                      'nor_pr': nor_pr,
                      'counts': counts,
                  },
                  )


def detail_povins(rq, povins_str):
    '''
    显示目标详情
    :param rq:
    :return:
    '''
    tklist = []
    for info in json_list:
        if info.get('province') == povins_str:
            tklist.append(info)
    # 已有数据数
    counts = len(tklist)
    # 异常数据
    # wor_infos = models.Rent12.objects.raw('select * from rent.rent_12 where (abs(rent_money-pred_money)/rent_money)>1')
    # 异常数量
    err_num = 0
    for info in tklist:
        if info in wor_infos:
            err_num += 1
    wor_num = err_num
    # 本页展示数量
    show_num = len(list(tklist[:30]))
    # 当前时间
    t_n = datetime.datetime.now().strftime('%H:%M:%S')
    # 异常占比
    wor_pr = round((wor_num / counts) * 100, 2)
    # 未展示
    also_has = counts - show_num
    # 正常
    normal = counts - wor_num
    # 正常占比
    nor_pr = 100 - wor_pr

    # posts = tklist
    if counts < 30:
        ONE_PAGE_OF_DATA = counts
    else:
        ONE_PAGE_OF_DATA = 30

    try:
        curPage = int(rq.GET.get('curPage', '1'))
        allPage = int(rq.GET.get('allPage', '1'))
        pageType = str(rq.GET.get('pageType', ''))
    except ValueError:
        curPage = 1
        allPage = 1
        pageType = ''

    # 判断点击了【下一页】还是【上一页】
    if pageType == 'pageDown':
        curPage += 1
    elif pageType == 'pageUp':
        curPage -= 1

    startPos = (curPage - 1) * ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    posts = tklist[startPos:endPos]

    if curPage == 1 and allPage == 1:  # 标记1
        allPostCounts = counts
        allPage = allPostCounts / ONE_PAGE_OF_DATA
        remainPost = allPostCounts % ONE_PAGE_OF_DATA
        if remainPost > 0:
            allPage += 1

    return render(rq,
                  'show/hole_list.html',
                  {
                      'posts': posts,
                      'wor_infos': wor_infos,
                      'wor_num': wor_num,
                      'show_num': show_num,
                      't_n': t_n,
                      'wor_pr': wor_pr,
                      'also_has': also_has,
                      'normal': normal,
                      'nor_pr': nor_pr,
                      'counts': counts,
                      'allPage': allPage,
                      'curPage': curPage,
                  },
                  )


def detail_regin(rq, region_str):
    '''
    显示目标详情
    :param rq:
    :return:
    '''

    tklist = []
    for info in json_list:
        if info.get('region') == region_str:
            tklist.append(info)
    # 已有数据数
    counts = len(tklist)
    # 异常数据
    # wor_infos = models.Rent12.objects.raw('select * from rent.rent_12 where (abs(rent_money-pred_money)/rent_money)>1')
    # 异常数量
    err_num = 0
    for info in tklist:
        if info in wor_infos:
            err_num += 1
    wor_num = err_num
    # 本页展示数量
    show_num = len(tklist[:100])
    # 当前时间
    t_n = datetime.datetime.now().strftime('%H:%M:%S')
    # 异常占比
    wor_pr = round((wor_num / counts) * 100, 2)
    # 未展示
    also_has = counts - show_num
    # 正常
    normal = counts - wor_num
    # 正常占比
    nor_pr = 100 - wor_pr

    # posts = tklist
    if counts < 30:
        ONE_PAGE_OF_DATA = counts
    else:
        ONE_PAGE_OF_DATA = 30

    try:
        curPage = int(rq.GET.get('curPage', '1'))
        allPage = int(rq.GET.get('allPage', '1'))
        pageType = str(rq.GET.get('pageType', ''))
    except ValueError:
        curPage = 1
        allPage = 1
        pageType = ''

    # 判断点击了【下一页】还是【上一页】
    if pageType == 'pageDown':
        curPage += 1
    elif pageType == 'pageUp':
        curPage -= 1

    startPos = (curPage - 1) * ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    posts = tklist[startPos:endPos]

    if curPage == 1 and allPage == 1:  # 标记1
        allPostCounts = counts
        allPage = allPostCounts / ONE_PAGE_OF_DATA
        remainPost = allPostCounts % ONE_PAGE_OF_DATA
        if remainPost > 0:
            allPage += 1

    return render(rq,
                  'show/hole_list.html',
                  {
                      'posts': posts,
                      'wor_infos': wor_infos,
                      'wor_num': wor_num,
                      'show_num': show_num,
                      't_n': t_n,
                      'wor_pr': wor_pr,
                      'also_has': also_has,
                      'normal': normal,
                      'nor_pr': nor_pr,
                      'counts': counts,
                      'allPage': allPage,
                      'curPage': curPage,
                  },
                  )
