#!/usr/bin/env python3

import argparse
import json
import os, os.path
import sys
import tornado.ioloop
import tornado.web
import os.path

# Argument parsing
parser = argparse.ArgumentParser(help="""RESTful server for rendering PDFs to SVGs (and PNGs)""")
parser.add_argument("--workdir", help="""Working directory where incoming PDFs and outgoing SVGs are stored""")
args = parser.parse_args()

# Create structure in workdir
if not os.path.exists(args.workdir):
    print("Error: Workdir does not exist")
    sys.exit(1)
INDIR = "in"
OUTDIR = "out"
for path in [INDIR, OUTDIR]:
    path = os.path.join(args.workdir, path)
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        if os.listdir(path) != 0:
            print("Error: Workdir is tainted. Try clearing the workdir.")
            sys.exit(1)

# Render job status
STATUS_PENDING = "PENDING"
STATUS_PROCESSING = "PROCESSING"
STATUS_DONE = "DONE"

jobs = []
nextId = 1
currentJob = None

class RenderJob:
    ID = -1
    status = None

    def __init__(self, ID : int, status: str):
        self.ID = ID
        self.status = status
    
    def __repr__(self):
        return "Job {} [{}]".format(self.ID, self.status)

class JobHandler(tornado.web.RequestHandler):
    def get(self, ID=None):
        result = {}
        if(ID is None):
            result["jobs"] = []
            for job in jobs:
                result["jobs"].append(job.id)
        else:
            try:
                ID = int(ID)
            except:
                self.set_status(404, "Invalid Job ID {}".format(ID))
                self.finish()
                return
            job = list(filter(lambda j: j.ID == ID, jobs))
            if not job:
                self.set_status(404, "Job {} is unknown".format(ID))
                self.finish()
                return
            job = job[0]
            result["ID"] = job.ID
            result["status"] = job.status
        
        self.finish(json.dumps(result))
    
    def post(self):
        pass

def make_app():
    return tornado.web.Application([
        (r"/job/?", JobHandler),
        (r"/job/([0-9]+)?", JobHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()