package main

func combinations[T any](items []T, r int) [][]T {
	if r == 0 {
		return [][]T{{}} // Base case: one empty combination
	}
	if len(items) == 0 {
		return nil
	}

	result := [][]T{}
	// Take the first item and find combinations of the rest
	first := items[0]
	remaining := items[1:]

	// Combinations including 'first' (r-1 more needed from remaining)
	for _, comb := range combinations(remaining, r-1) {
		result = append(result, append([]T{first}, comb...))
	}

	// Combinations excluding 'first' (r more needed from remaining)
	result = append(result, combinations(remaining, r)...)

	return result
}

// Helper to get all combinations of all lengths (powerset)
func all_combinations[T any](items []T) [][]T {
	var all [][]T
	for i := 0; i <= len(items); i++ {
		all = append(all, combinations(items, i)...)
	}
	return all
}
