function gata_data(){
//     $(function(){
//     $('#txtResult').change(function () {
//         var value = $(this).val();
//         console.log(value)
//     })
// });
 <!--百度地图api功能-->

    var map = new BMap.Map('container');  // 创建Map实例
    var point = new BMap.Point(116.404, 39.915);  // 设置坐标中心点
    map.centerAndZoom(point, 11);  // 地图初始化，设置展示级别


    map.addEventListener("click", function (e) {
        alert("当前位置：" + e.point.lng + ", " + e.point.lat);
    });


    function $(id) {
        return document.getElementById(id);//定义$,以便调用
    }

    function searcha() {
        $("txtResult").value = "";  // 每次生成前清空文本域
        map.clearOverlays();    //清除地图上所有覆盖物
        var c = $("txtCity").value;

        var point = new BMap.LocalSearch(map, {
            renderOptions: {map: map}
        });

        point.search(c);   // 查找城市

        var s = $("txtSearch").value;  // 获得输入的关键字

        var ls = new BMap.LocalSearch(c);  // 创建城市c的检索
        ls.search(s);   // 城市搜索关键字

        var i = 1;
        ls.setSearchCompleteCallback(function (results) {
            if (ls.getStatus() == BMAP_STATUS_SUCCESS) {
                for (j = 0; j < results.getCurrentNumPois(); j++) {  // 遍历第一页
                    var poi = results.getPoi(j);

                    map.addOverlay(new BMap.Marker(poi.point)); //如果查询到，则添加红色marker
                    $("txtResult").value += poi.title + ":" + poi.point.lng + "," + poi.point.lat + poi.phoneNumber + '\n';
                }
                // var currPage = results.getPageIndex();// 获取当前是第几页数据
                // console.log(currPage);

                if (results.getPageIndex != results.getNumPages()) {
                    ls.gotoPage(i);
                    i = i + 1;
                }
            }
            // window.totalResults = results.getNumPois();
            // window.totalPages = results.getNumPages();
            // console.log("totalResults:" + totalResults + ' ' + 'totalPages:' + totalPages);
        });


    }

    // searcha(); //onclick="searcha()"


    // 添加地图类型控件
    map.addControl(new BMap.MapTypeControl({
        mapTypes: [
            BMAP_NORMAL_MAP,
            BMAP_HYBRID_MAP
        ]
    }));
    map.setCurrentCity("北京");          // 设置地图显示的城市 此项是必须设置的
    map.enableScrollWheelZoom(true);     //开启鼠标滚轮缩放

    window.setTimeout(function () {
        map.panTo(new BMap.Point(116.404, 39.918));

    }, 2000);       //  设置2s后滑动到新的中心点


    //加一个平移缩放控件、一个比例尺控件和一个缩略图控
    map.addControl(new BMap.NavigationControl());
    map.addControl(new BMap.ScaleControl());
    map.addControl(new BMap.OverviewMapControl());
    map.addControl(new BMap.MapTypeControl());

    //添加监听事件，显示点击的坐标
    // map.addEventListener("click", function(e){
    // alert(e.point.lng + ", " + e.point.lat);
    // });





alert('lalal');
var value = $('txtCity').val();
    if (value){
        console.log(value);
        return true
    }
    else{
        console.log('空');
        return false
    }


}

