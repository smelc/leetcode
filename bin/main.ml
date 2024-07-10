let merge_nodes_between_zeros() =
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

let () = 
  merge_nodes_between_zeros();
  print_endline "Hello, World!"
