#!/usr/bin/env python3

import sys, os, re ,json , subprocess, requests
from subprocess import check_output, run
import queue
from json.decoder import JSONDecodeError
from sys import exit
import asyncio
import aiohttp

exit_status = 0

async def task(location, work_queue, root_folder):
    global exit_status
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            package = await work_queue.get()
            async with session.post('http://paws-backend.ap-southeast-2.elasticbeanstalk.com/threat/search',json={"package_manager_type" : "npm","package_list" : [package],"level": 0, "severity": ["CRITICAL"], "date": "None"}) as r:
                if r.status == 200:
                    r_content = await r.json()
                    for h in r_content:
                        if len(r_content[h][1]) != 0:
                            file_name = h + '_vulnerabilities.json'
                            path = root_folder+"/"+file_name
                            data = {}
                            data[h] = r_content[h][1]
                            with open(path, 'w') as outfile:
                                json.dump(data, outfile)
                            outfile.close()
                            print("The package {} in your {} is vulnerable. Please go to {} to find out more".format(h,location,file_name))
                            exit_status = 1
                        
async def main():
    global exit_status
    result = run(
            ["git", "rev-parse", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False
        )
    
    root_folder = run(["git", "rev-parse", "--show-toplevel"],stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False).stdout.decode("utf-8").strip()
    
    if result.stdout.decode("utf-8") == "HEAD":
        file_to_commit = check_output([ 'git', 'diff', '--cached', '--name-status' , 'HEAD'])
    else:
        file_to_commit = check_output([ 'git', 'diff', '--cached', '--name-status'])
    file_to_commit = file_to_commit.decode("utf-8")
    file_to_commit = file_to_commit.replace("M\t", " ")
    file_to_commit = file_to_commit.replace("C\t", " ")
    file_to_commit = file_to_commit.replace("R\t", " ")
    file_to_commit = file_to_commit.replace("A\t", " ")
    file_to_commit = file_to_commit.replace("U\t", " ")
    file_to_commit = file_to_commit.strip()
    file_to_commit = file_to_commit.split(" ")
    
    for i in file_to_commit:
        if "D\t" in i.strip():
            continue
        if "package.json" in i.strip():
            if os.stat(i.strip()).st_size == 0:
                print("WARNING:\tYour file {} is empty. You may want to check that you did not make a mistake".format(i.strip()))
            else:
                f = open(i.strip(),)
                try:
                    data = json.load(f)
                    if "dependencies" in data:
                        work_queue = asyncio.Queue()
                        package_list = list(data["dependencies"].keys())
                        for package in package_list:
                            await work_queue.put(package)
                        print("Scanning your dependencies. Please hold on tight")
                        await asyncio.gather(asyncio.create_task(task("dependencies",work_queue,root_folder)),asyncio.create_task(task("dependencies",work_queue,root_folder)),asyncio.create_task(task("dependencies",work_queue,root_folder)),asyncio.create_task(task("dependencies",work_queue,root_folder)),asyncio.create_task(task("dependencies",work_queue,root_folder)))
                    if "devDependencies" in data:
                        work_queue = asyncio.Queue()
                        package_list = list(data["devDependencies"].keys())
                        for package in package_list:
                            await work_queue.put(package)
                        print("Scanning your devdependencies. Please hold on tight")
                        await asyncio.gather(asyncio.create_task(task("devDependencies",work_queue,root_folder)),asyncio.create_task(task("devDependencies",work_queue,root_folder)),asyncio.create_task(task("devDependencies",work_queue,root_folder)),asyncio.create_task(task("devDependencies",work_queue,root_folder)),asyncio.create_task(task("devDependencies",work_queue,root_folder)))
                    f.close()
                    if (exit_status == 1):
                        print("You have some files with critical vulnerbilities, please solve those before commiting again.")
                except JSONDecodeError:
                    print("WARNING:\tYour file {} is not readable as a json file. Please check that you did not make a mistake".format(i.strip()))
                    f.close()
                    exit_status =1
    exit(exit_status)

if __name__ == "__main__":
    asyncio.run(main())
