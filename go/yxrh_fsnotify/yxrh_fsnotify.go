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

func (w *Watch) watchDir(dir string) {
	filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
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
						fi, err := os.Stat(ev.Name)
						if err == nil && fi.IsDir() {
							w.watch.Remove(ev.Name)
							logger.Alert("删除监控 : ", ev.Name)
						}
					}
					if ev.Op&fsnotify.Rename == fsnotify.Rename {
						logger.Alert("重命名文件 : ", ev.Name)
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
	logger.SetLogger(`{"Console":{"level":"INFO"},"File": {"filename":"/var/log/fsnotify.log","level": "ALRT","maxlines": 1000000,"maxsize": 1,"maxdays": -1,"append": true,"permit": "0664"}}`)
	fmt.Scanln(&dirname1, &dirname2, &dirname3, &dirname4, &dirname5, &dirname6, &dirname7, &dirname8, &dirname9, &dirname10, &dirname11, &dirname12, &dirname13, &dirname14, &dirname15, &dirname16, &dirname17, &dirname18, &dirname19, &dirname20, &dirname21, &dirname22, &dirname23, &dirname24, &dirname25)
	dirs_s = append(dirs_s, dirname1, dirname2, dirname3, dirname4, dirname5, dirname6, dirname7, dirname8, dirname9, dirname10, dirname11, dirname12, dirname13, dirname14, dirname15, dirname16, dirname17, dirname18, dirname19, dirname20, dirname21, dirname22, dirname23, dirname24, dirname25)
	watch, _ := fsnotify.NewWatcher()
	w := Watch{
		watch: watch}
	for index := 0; index < 25; index++ {
		if dirs_s[index] == "" {
			break
		}

		w.watchDir(dirs_s[index])
	}
	select {}
}
