"use client"

import { CustomDataTable } from "@/components/custom-data-table/custom-data-table";
import { columns } from "@/components/custom-data-table/columns";
import { useProfessionals } from "@/hooks/use-professionals";


export default function Page() {
    const { data, isLoading, error } = useProfessionals();

    if (isLoading) return <div>Loading...</div>;
    if (error) return <div>Error loading professionals</div>;

    return (
        <section className="flex-1">
            <CustomDataTable columns={columns} data={data ?? []} />
        </section>
    );
}