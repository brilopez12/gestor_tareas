<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Task;


class TaskController extends Controller
{
    public function index()
    {
        return Task::all();
    }

    public function store(Request $request)
    {   
        $task = new Task();
        $task->title = $request->title;
        $task->description = $request->description;
        $task->start_date = $request->start_date;
        $task->end_date = $request->end_date;
        $task->status = $request->status;
        $task->save();
        return response()->json($task, 201);
    }

    public function show($id)
    {
        //
    }
    /*public function edit(string $id)
    {
        //
        $task = Task::find($id);
    }*/
    public function update(Request $request, $id)
    {   
        $task = Task::find($id);
        $task->title = $request->title;
        $task->description = $request->description;
        $task->start_date = $request->start_date;
        $task->end_date = $request->end_date;
        $task->status = $request->status;
        $task->save();
        return response()->json($task, 200);
    }

    public function destroy($id)
    {
        $task = Task::find($id);
        $task->delete();
        return response()->json(null, 204);
    }
}


