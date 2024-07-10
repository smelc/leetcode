let _merge_nodes_between_zeros() =
  let print_it (l : int list) : string = 
    let rec go_print = function
        | [] -> ""
        | x :: [] -> string_of_int x
        | x :: rest -> (string_of_int x) ^ ", " ^ (go_print rest) in
    "[" ^ (go_print l) ^ "]"
  in
  let rec go l acc =
    match l with 
      | 0 :: [] -> [acc]
      | 0 :: rest -> [acc] @ (go rest 0)
      | hd :: rest -> go rest (hd + acc)
      | _ -> assert false
    in
  let go_first = function
      | 0 :: rest -> go rest 0
      | _ -> assert false in
  let l = [0; 3; 1; 0; 4; 5; 2; 0] in
  print_endline @@ print_it l;
  print_endline @@ print_it @@ go_first l;
  let l = [0; 333; 711; 0; 941; 0; 614; 0; 387; 0; 245; 573; 0; 162; 710; 101; 0; 709; 795; 774; 0; 198; 773; 0; 731; 0; 962; 0; 881; 891; 886; 955; 294; 0; 601; 374; 0; 625; 0; 271; 0; 665; 0; 651; 413; 0; 767; 0; 617; 0; 837; 0; 521; 0; 476; 114; 0; 364; 154; 0; 744; 0; 13; 967; 0; 908; 149; 219; 0; 109; 483; 731; 0] in
  print_endline @@ print_it l;
  print_endline @@ print_it @@ go_first l

let average_waiting_time (l: (int * int) list) : float = 
  let rec go (current_time:float) (l: (int * int) list) acc : float list =
    match l with
      | [] -> acc
      | (arrival_time, prep_time) :: l_rest ->
        let current_time: float = Float.(max current_time @@ of_int arrival_time) in
        let finish_time: float = Float.(add current_time @@ of_int prep_time) in
        let waiting_time: float = Float.(sub finish_time @@ of_int arrival_time) in
        go finish_time l_rest (waiting_time :: acc)
    in
  let rec sum_floats = function
    | [] -> 0.0
    | f :: rest -> Float.add f @@ sum_floats rest in
  let float_waiting_times: float list = go 0.0 l [] in
  Float.(div (sum_floats float_waiting_times) (Float.of_int @@ List.length float_waiting_times))

let _float_list_to_string l =
  let rec go = function
    | [] -> ""
    | [f] -> Float.to_string f
    | f :: l_rest -> Float.to_string f ^ go l_rest in
  "[" ^ go l ^ "]"

let () = 
  (* _merge_nodes_between_zeros(); *)
  print_endline @@ Float.to_string @@ average_waiting_time [(5,2); (5,4); (10,3); (20,1)];
  print_endline "Hello, World!"
