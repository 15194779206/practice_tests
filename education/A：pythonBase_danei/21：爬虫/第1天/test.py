html='''
<dl class="board-wrapper">
    <div class="board-item-content">
        <div class="movie-item-info">
            <p class="name">
                <a href="/films/1328712" title="我和我的家乡" data-act="boarditem-click" data-val="{movieId:1328712}">我和我的家乡</a>
            </p>
            <p class="star">主演：刘昊然,葛优,刘敏涛</p><p class="releasetime">上映时间：2020-10-01</p>    
        </div>
        <div class="movie-item-number wish">
            <p class="month-wish">本月新增想看：<span><span class="stonefont"></span></span>人</p>
            <p class="total-wish">总想看：<span><span class="stonefont"></span></span>人</p>
        </div>
    </div>
</dl>
'''
import re
pattern =re.compile('<div class="board-item-content">(.*?)</div>')
re_list = pattern.findall(html)
print(re_list)