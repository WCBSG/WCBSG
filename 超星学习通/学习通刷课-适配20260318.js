const activeElement = $(".posCatalog_select.posCatalog_active");

if (activeElement.length) {
    const chapterTitles = $(".posCatalog_select:has(.posCatalog_title)");
    const substantiveSiblings = $(".posCatalog_select").not(chapterTitles);
    let unitCount = substantiveSiblings.index(activeElement);
    unitCount += 1;
    if (!substantiveSiblings.length || unitCount === -1) {
        console.warn("未找到有效的.posCatalog_select同级元素！");
        unitCount = -1;
    }
    window.unitCount = unitCount;
} else {
    console.error("未找到激活的小节元素！");
}
window.unit = $(".posCatalog_level span em").length;
function main() {
    document.querySelector('li[title="视频"]').click();
    setTimeout(() => {
        const frameObj = $("iframe").eq(0).contents().find("iframe.ans-insertvideo-online");
        const videoNum = frameObj.length;
        if (videoNum > 0) {
            console.log("%c当前小节中包含 " + videoNum + " 个视频", "color:#FF7A38;font-size:18px");
            var v_done = 0;
            addEventListener("playdone", () => {
                v_done++;
                if (v_done > videoNum) {
                } else if (v_done < videoNum) {
                    watchVideo(frameObj, v_done)
                } else {
                    console.log("%c本小节视频播放完毕，等待跳转至下一小节...", "font-size:18px");
                    nextUnit();
                }
            });
            watchVideo(frameObj, v_done);
        } else {
            if (window.unitCount < window.unit) {
                console.log("%c当前小节中无视频，6秒后将跳转至下一节", "font-size:18px");
                nextUnit();
            } else {
                console.log("%c好了好了，毕业了", "color:red;font-size:18px");
            }
        }
    }, 3000);// 3000毫秒（即3秒）后执行
}
function watchVideo(frameObj, v_done) {
    var playDoneEvent = new Event("playdone");
    var v = undefined;
    v = frameObj.contents().eq(v_done).find("video#video_html5_api").get(0);
    window.a = v;
    try {
        v.playbackRate = 1.5;
    } catch (e) {
        console.error("倍速设置失败！此节可能有需要回复内容，不影响，跳至下一节。错误信息：" + e);
        nextUnit();
        return;
    }
    v.play();
    console.log("%c正在 " + v.playbackRate + " 倍速播放第 " + (v_done + 1) + " 个视频", "font-size:18px");
    window.inter = setInterval(() => {
        v = window.a;
        if (v.currentTime >= v.duration) {
            dispatchEvent(playDoneEvent);
            clearInterval(window.inter);
        }
        if (v.paused) {
            v.play();
        }
    }, 1000);
}
function nextUnit() {
    console.log("%c即将进入下一节...", "color:red;font-size:18px");
    setTimeout(() => {
        $(document).scrollTop($(document).height() - $(window).height());
        $("#prevNextFocusNext").click()
        $(".nextChapter").eq(0).click()
        $("#prevNextFocusNext").click()
        $(".nextChapter").eq(0).click()
        if (window.unitCount++ < window.unit) {
            setTimeout(() => main(), 10000)
        }
    }, 6000);
}
console.log("%c 此科目有%c %d %c个小节，当前为 %c第%d小节 %c-chao", "color:#6dbcff", "color:red", window.unit, "color:#6dbcff", "color:red", window.unitCount, "font-size:8px");
main();
