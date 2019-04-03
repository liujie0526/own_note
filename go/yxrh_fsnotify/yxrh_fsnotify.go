package main

import (
	"fmt"
	"os"
	"path/filepath"

	"github.com/fsnotify/fsnotify"
	"github.com/wonderivan/logger"
)

type Watch struct {
	watch *fsnotify.Watcher
}

//监控目录
func (w *Watch) watchDir(dir string) {
	//通过Walk来遍历目录下的所有子目录
	filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		//这里判断是否为目录，只需监控目录即可
		//目录下的文件也在监控范围内，不需要我们一个一个加
		if info.IsDir() {
			path, err := filepath.Abs(path)
			if err != nil {
				return err
			}
			err = w.watch.Add(path)
			if err != nil {
				return err
			}
			logger.Info("监控 : ", path)
		}
		return nil
	})
	go func() {
		for {
			select {
			case ev := <-w.watch.Events:
				{
					if ev.Op&fsnotify.Create == fsnotify.Create {
						logger.Alert("创建文件 : ", ev.Name)
						//这里获取新创建文件的信息，如果是目录，则加入监控中
						fi, err := os.Stat(ev.Name)
						if err == nil && fi.IsDir() {
							w.watch.Add(ev.Name)
							logger.Alert("添加监控 : ", ev.Name)
						}
					}
					if ev.Op&fsnotify.Write == fsnotify.Write {
						logger.Alert("写入文件 : ", ev.Name)
					}
					if ev.Op&fsnotify.Remove == fsnotify.Remove {
						logger.Alert("删除文件 : ", ev.Name)
						//如果删除文件是目录，则移除监控
						fi, err := os.Stat(ev.Name)
						if err == nil && fi.IsDir() {
							w.watch.Remove(ev.Name)
							logger.Alert("删除监控 : ", ev.Name)
						}
					}
					if ev.Op&fsnotify.Rename == fsnotify.Rename {
						logger.Alert("重命名文件 : ", ev.Name)
						//如果重命名文件是目录，则移除监控
						//注意这里无法使用os.Stat来判断是否是目录了
						//因为重命名后，go已经无法找到原文件来获取信息了
						//所以这里就简单粗爆的直接remove好了
						w.watch.Remove(ev.Name)
					}
					if ev.Op&fsnotify.Chmod == fsnotify.Chmod {
						logger.Alert("修改权限 : ", ev.Name)
					}
				}
			case err := <-w.watch.Errors:
				{
					logger.Error("error : ", err)
					return
				}
			}
		}
	}()
}

var (
	dirname1  string
	dirname2  string
	dirname3  string
	dirname4  string
	dirname5  string
	dirname6  string
	dirname7  string
	dirname8  string
	dirname9  string
	dirname10 string
	dirname11 string
	dirname12 string
	dirname13 string
	dirname14 string
	dirname15 string
	dirname16 string
	dirname17 string
	dirname18 string
	dirname19 string
	dirname20 string
	dirname21 string
	dirname22 string
	dirname23 string
	dirname24 string
	dirname25 string

	dirs   [0]string
	dirs_s []string = dirs[:]
)

func main() {
	fmt.Scanln(&dirname1, &dirname2, &dirname3, &dirname4, &dirname5, &dirname6, &dirname7, &dirname8, &dirname9, &dirname10, &dirname11, &dirname12, &dirname13, &dirname14, &dirname15, &dirname16, &dirname17, &dirname18, &dirname19, &dirname20, &dirname21, &dirname22, &dirname23, &dirname24, &dirname25)
	dirs_s = append(dirs_s, dirname1, dirname2, dirname3, dirname4, dirname5, dirname6, dirname7, dirname8, dirname9, dirname10, dirname11, dirname12, dirname13, dirname14, dirname15, dirname16, dirname17, dirname18, dirname19, dirname20, dirname21, dirname22, dirname23, dirname24, dirname25)
	//	time.Sleep(15 * time.Second)
	watch, _ := fsnotify.NewWatcher()
	w := Watch{
		watch: watch}
	//	w.watchDir("/tmp/home")
	for index := 0; index < 25; index++ {
		if dirs_s[index] == "" {
			break
		}

		//		logger.Error(dirs_s[index])
		//		go func() {
		w.watchDir(dirs_s[index])
		//		}()
	}
	select {}
}
