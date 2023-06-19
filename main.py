import os

import sublime
import sublime_plugin
import subprocess


def readFile(fn):
    with open(fn, 'r') as fp:
        return fp.read().strip()


def getCurrentPID():
    fn = sublime.active_window().active_view().file_name()
    dir = os.path.dirname(fn)

    for _ in range(12):
        dirs = os.listdir(dir)
        if 'flutter.pid' in dirs:
            pid = readFile(os.path.join(dir, 'flutter.pid'))
            return pid
        else:
            dir = os.path.dirname(dir)
    return None


class FlutterHotReloadCommand(sublime_plugin.WindowCommand):

    def run(self):
        print(dir(self))
        pid = getCurrentPID()
        subprocess.call(["bash", "-c", "kill -SIGUSR1 {}".format(pid)])


class FlutterHotRestartCommand(sublime_plugin.WindowCommand):
    def run(self):
        pid = getCurrentPID()
        subprocess.call(["bash", "-c", "kill -SIGUSR2 {}".format(pid)])


class FlutterHotReloadWhenSaved(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        view.window().run_command("flutter_hot_reload")
